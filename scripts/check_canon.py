#!/usr/bin/env -S uv run --quiet
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Consistency checker for the Neederlandsch Schuijnvaerders Gilde knowledge base.

Run with:  uv run scripts/check_canon.py [--strict-tbd] [--root DIR]
Self-test: uv run scripts/check_canon.py --self-test

Checks, in order:
  1. canon/facts.yaml parses; TBD values are listed (a failure only with --strict-tbd).
  2. Every Markdown file under brand/, lore/, csrd/, agents/, policies/ has frontmatter with
     title, status, last-verified and canon-refs; every canon-ref exists in canon and
     its value appears in the body.
  3. No word or phrase from canon/anachronisms.txt appears in prose (whole word,
     case-insensitive), outside fenced code, outside <!-- ooc --> ... <!-- /ooc --> blocks,
     unless the file's frontmatter lists it under allow-anachronisms. Files under
     lore/research/ are the plain-English historical record and are exempt from this
     check and from the numeric guards (they still need frontmatter and valid links).
  4. Every guard in canon/guards.yaml (a regex with one numeric capture) agrees with the
     canon value it names, wherever the pattern matches in prose.
  5. Every relative Markdown link resolves to an existing file.
  6. Every data/*.csv has a sibling *.schema.md whose ```columns block equals the CSV header.
Exit code 0 when clean, 1 when any error was found, 2 on usage or environment problems.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "PyYAML is not installed for this interpreter. Run the checker with\n"
        "    uv run scripts/check_canon.py\n"
        "which resolves the dependency from the script header.\n"
    )
    sys.exit(2)

PROSE_DIRS = ("brand", "lore", "csrd", "agents", "policies")
RECORD_DIRS = ("lore/research",)  # plain-English record of real history: frontmatter and links only
ROOT_PROSE_FILES = ("AGENTS.md", "README.md")
REQUIRED_FM = ("title", "status", "last-verified", "canon-refs")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE_RE = re.compile(r"```.*?```", re.S)
OOC_RE = re.compile(r"<!--\s*ooc\s*-->.*?<!--\s*/ooc\s*-->", re.S | re.I)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, line: int | None, msg: str) -> None:
        loc = f"{path}:{line}" if line else str(path)
        self.errors.append(f"{loc}: {msg}")

    def warn(self, path: Path, line: int | None, msg: str) -> None:
        loc = f"{path}:{line}" if line else str(path)
        self.warnings.append(f"{loc}: {msg}")


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def canon_lookup(canon: dict, dotted: str):
    """Resolve 'a.b.0.c' or 'bases[key=vlissingen].name' against the canon mapping."""
    cur = canon
    for part in re.split(r"\.(?![^\[]*\])", dotted):
        m = re.fullmatch(r"(\w+)\[(\w+)=([^\]]+)\]", part)
        if m:
            cur = cur[m.group(1)]
            cur = next(item for item in cur if str(item.get(m.group(2))) == m.group(3))
            continue
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def value_forms(value) -> list[str]:
    """Strings a canon value may legitimately take in prose."""
    if isinstance(value, bool):
        return [str(value).lower(), str(value)]
    if isinstance(value, int):
        forms = {str(value), f"{value:,}"}
        if value >= 1_000_000 and value % 1_000_000 == 0:
            forms.add(f"{value // 1_000_000} million")
        return sorted(forms)
    if isinstance(value, float):
        return [str(value), f"{value:g}"]
    return [str(value)]


def find_tbd(node, path: str = "") -> list[str]:
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            out += find_tbd(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out += find_tbd(v, f"{path}.{i}")
    elif isinstance(node, str) and node.strip().upper() == "TBD":
        out.append(path)
    return out


def strip_non_prose(body: str) -> str:
    """Blank out fenced code, inline code and out-of-character blocks, keeping line numbers."""
    def blank(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    body = FENCE_RE.sub(blank, body)
    body = OOC_RE.sub(blank, body)
    body = INLINE_CODE_RE.sub(blank, body)
    return body


def load_list(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")]


def check_prose_file(path: Path, root: Path, canon: dict, anachronisms: list[str],
                     guards: list[dict], rep: Report, require_fm: bool) -> None:
    text = path.read_text(encoding="utf-8")
    is_record = any(path.resolve().is_relative_to((root / d).resolve()) for d in RECORD_DIRS)
    if is_record:
        anachronisms, guards = [], []
    fm: dict = {}
    body = text
    m = FM_RE.match(text)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            rep.error(path, 1, f"frontmatter is not valid YAML: {exc}")
            fm = {}
        body = text[m.end():]
        body_offset = m.end()
    else:
        body_offset = 0
        if require_fm:
            rep.error(path, 1, "missing frontmatter (--- title/status/last-verified/canon-refs ---)")

    if m and require_fm:
        for key in REQUIRED_FM:
            if key not in fm:
                rep.error(path, 1, f"frontmatter lacks required key '{key}'")
        if "canon-refs" in fm and not isinstance(fm["canon-refs"], list):
            rep.error(path, 1, "frontmatter 'canon-refs' must be a list")

    # canon refs
    for ref in (fm.get("canon-refs") or []) if isinstance(fm.get("canon-refs"), list) else []:
        try:
            value = canon_lookup(canon, str(ref))
        except (KeyError, IndexError, StopIteration, ValueError, TypeError):
            rep.error(path, 1, f"canon-ref '{ref}' does not exist in canon/facts.yaml")
            continue
        if isinstance(value, (dict, list)):
            continue  # structural refs are allowed as a pointer only
        if not any(form in body for form in value_forms(value)):
            rep.error(path, 1, f"canon-ref '{ref}' = {value!r} is declared but never appears in the body")

    prose = strip_non_prose(body)

    # anachronisms
    allowed = {str(a).lower() for a in (fm.get("allow-anachronisms") or [])}
    for word in anachronisms:
        if word.lower() in allowed:
            continue
        pat = re.compile(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", re.I)
        for hit in pat.finditer(prose):
            rep.error(path, line_of(body, hit.start()) + text.count("\n", 0, body_offset),
                      f"anachronism '{hit.group(0)}' (allow it in frontmatter with a reason, or wrap in <!-- ooc --> ... <!-- /ooc -->)")

    # guards
    for g in guards:
        try:
            expected = canon_lookup(canon, g["canon_key"])
        except Exception:
            rep.error(root / "canon" / "guards.yaml", None, f"guard canon_key '{g['canon_key']}' not in canon")
            continue
        pat = re.compile(g["pattern"], re.I)
        for hit in pat.finditer(prose):
            raw = hit.group(1).replace(",", "").replace(".", "")
            if not raw.isdigit():
                continue
            found = int(raw) * int(g.get("multiply", 1))
            if found != int(expected):
                rep.error(path, line_of(body, hit.start()) + text.count("\n", 0, body_offset),
                          f"'{hit.group(0)}' disagrees with canon {g['canon_key']} = {expected}")

    # links
    for hit in LINK_RE.finditer(body):
        target = hit.group(1)
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            rep.error(path, line_of(body, hit.start()) + text.count("\n", 0, body_offset),
                      f"broken relative link '{target}'")


def check_csvs(root: Path, rep: Report) -> None:
    for csv_path in sorted((root / "data").glob("*.csv")) if (root / "data").exists() else []:
        schema = csv_path.with_suffix(".schema.md")
        if not schema.exists():
            rep.error(csv_path, None, f"no sibling schema file {schema.name}")
            continue
        m = re.search(r"```columns\n(.*?)```", schema.read_text(encoding="utf-8"), re.S)
        if not m:
            rep.error(schema, None, "schema has no ```columns block")
            continue
        expected = [c.strip() for c in m.group(1).splitlines() if c.strip()]
        with csv_path.open(encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, [])
            width = len(header)
            for n, row in enumerate(reader, start=2):
                if row and len(row) != width:
                    rep.error(csv_path, n, f"row has {len(row)} fields, header has {width}")
        if header != expected:
            rep.error(csv_path, 1, f"header {header} != schema columns {expected}")


def run(root: Path, strict_tbd: bool) -> Report:
    rep = Report()
    canon_path = root / "canon" / "facts.yaml"
    if not canon_path.exists():
        rep.error(canon_path, None, "canon file missing")
        return rep
    try:
        canon = yaml.safe_load(canon_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        rep.error(canon_path, None, f"canon does not parse: {exc}")
        return rep

    for tbd in find_tbd(canon):
        (rep.error if strict_tbd else rep.warn)(canon_path, None, f"TBD value at {tbd}")

    anachronisms = load_list(root / "canon" / "anachronisms.txt")
    guards_path = root / "canon" / "guards.yaml"
    guards = (yaml.safe_load(guards_path.read_text(encoding="utf-8")) or []) if guards_path.exists() else []

    files: list[tuple[Path, bool]] = []
    for d in PROSE_DIRS:
        if (root / d).exists():
            files += [(p, True) for p in sorted((root / d).rglob("*.md"))]
    for name in ROOT_PROSE_FILES:
        if (root / name).exists():
            files.append((root / name, False))
    for path, require_fm in files:
        check_prose_file(path, root, canon, anachronisms, guards, rep, require_fm)

    check_csvs(root, rep)
    return rep


def self_test(script_dir: Path) -> int:
    fixtures = script_dir / "fixtures"
    clean = run(fixtures / "clean", strict_tbd=False)
    if clean.errors:
        print("SELF-TEST FAILED: clean fixture produced errors:")
        print("\n".join("  " + e for e in clean.errors))
        return 1
    bad = run(fixtures / "bad", strict_tbd=False)
    expected_markers = ["anachronism", "broken relative link", "disagrees with canon",
                        "missing frontmatter", "!= schema columns", "never appears in the body"]
    missing = [mk for mk in expected_markers if not any(mk in e for e in bad.errors)]
    if missing:
        print("SELF-TEST FAILED: bad fixture did not trigger:", ", ".join(missing))
        print("\n".join("  " + e for e in bad.errors))
        return 1
    print(f"self-test ok: clean fixture passes, bad fixture raises {len(bad.errors)} errors covering all {len(expected_markers)} classes")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=None, help="repository root (default: parent of scripts/)")
    ap.add_argument("--strict-tbd", action="store_true", help="treat TBD canon values as errors")
    ap.add_argument("--self-test", action="store_true", help="run against scripts/fixtures and exit")
    args = ap.parse_args()
    script_dir = Path(__file__).resolve().parent
    if args.self_test:
        return self_test(script_dir)
    root = Path(args.root).resolve() if args.root else script_dir.parent
    rep = run(root, args.strict_tbd)
    for w in rep.warnings:
        print("warning:", w)
    for e in rep.errors:
        print("error:", e)
    print(f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
