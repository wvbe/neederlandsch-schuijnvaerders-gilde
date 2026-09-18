# Implementation Plan: Pirate Shipping Inc — brand, backstory and CSRD knowledge base

## Overview

Build a self-contained knowledge base for **Neederlandsch Schuijnvaerders Gilde N.V.** (NSG; English trade name *Pirate Shipping Inc*), a fictitious
cargo and "contracted interdiction" company that operates today with nothing but
17th-century technology and speaks only in pirate speak. The repository is the single
source of truth other agents will use to report on CSRD (ESRS) for PSI through the
Salacia platform. Deliverables are prose, structured data and agent instructions — not
application code. The one piece of code is a small consistency checker so that "did we
build the right thing" can be verified mechanically for a docs repository.

Fixed facts from the brief:

| Fact | Value |
| --- | --- |
| Fleet | ~25 wooden ships, anywhere in the world at any time |
| Bases | 5, across the operating regions |
| Regions | Netherlands, UK, Ireland, Caribbean, Indian Ocean, South East Asia, Pacific islands |
| Cargo | Spices, valuables, exotic materials; anything high-risk |
| Side business | Contracted disruption / seizure of other freighters' cargo |
| Technology | Strictly 17th century (sail, hemp, tar, backstaff, dead reckoning, gunpowder) |
| Language | Pirate speak, everywhere |
| Purpose | Demo/test tenant that reports CSRD via Salacia, written by other agents |

## What Salacia needs from a reporting organization

Taken from the Salacia knowledge base (`salacia-context` skill, domain-model and
reporting-standards notes). The PSI knowledge base must be able to feed each of these.

| Salacia concept | What PSI must define |
| --- | --- |
| Organization (name, reporting-year start month, enabled products) | Legal name, fiscal year, which products are on (CSRD topics, DMA, surveys) |
| Reporting year (`mmyyyy-mmyyyy`, per-year legal entities) | Which year is reported, base year, entities that exist in that year |
| Legal entity → location | The holding plus one entity per base; bases and ships as locations |
| E1 activity data (quantity, unit, period → emission factor → scope) | Fuel-like consumption per ship/base: firewood, charcoal, tar, gunpowder, lamp oil, tallow |
| Double materiality (topics → IROs scored → thresholds) | Materiality topics, impacts/risks/opportunities with scores |
| Surveys (schema → deployment → assignment → answer + evidence) | Who answers for which base/ship; what evidence a 17th-century company can produce |
| Reduction plan (targets, pathways, projects) | Targets that make sense for a company with no engines |
| ESRS topic answers (ESRS 2, E1–E5, S1–S4, G1) | One knowledge file per topic with facts, numbers and narrative hooks |
| VSME composition (B/C modules from E1/E3/plan data) | Falls out of the above; no separate work |

## Architecture decisions

1. **Canon file is the only place numbers live.** `canon/facts.yaml` holds every
   number and proper noun that must stay consistent (fleet size, base names, headcount,
   turnover, founding year, reporting year, entity names). Prose quotes canon; it never
   invents a competing figure. A checker script enforces it.
2. **Pirate speak in prose, standard identifiers untouched.** Numbers, units, currency
   codes, dates, ESRS codes, datapoint identifiers, legal entity names and ISO country
   codes are written the standard way so Salacia (and a spreadsheet parser) can read
   them. Everything around them is pirate speak. The style guide defines the boundary.
3. **Three registers of pirate speak.** Formal (regulatory report narrative), internal
   (logbooks, articles, ship-to-ship), and marketing (brand voice). Same lexicon, different
   density. Reports must remain intelligible to an auditor.
4. **Historically grounded, then bent.** Real pirate practice (articles of agreement,
   share-based pay, injury compensation schedules, elected captains, quartermaster as
   counterweight, careening, letters of marque, Tortuga/Nassau/Madagascar bases, the Dutch
   VOC/WIC context) is researched first with sources, then woven into the backstory. The
   research dossier records what is real and what is invented.
5. **The "stuck in time" mechanism is a company rule, not magic.** PSI is a real modern
   legal entity (EU-registered, so CSRD applies) whose founding articles forbid any
   technology not in use aboard a Dutch fluyt in the 1600s. The backstory explains how a
   17th-century company survived, incorporated and got large enough to be in CSRD scope.
6. **In scope of CSRD on purpose.** PSI is sized above the revised large-undertaking
   thresholds (over 1,000 employees and over EUR 450M turnover; Task 1 verifies the
   current Omnibus values and records them in canon with the date checked): about 2,300
   people and about EUR 480M turnover, so the reporting story is not undermined by scope
   questions.
7. **Ethical guardrails baked into the lore.** The interdiction business is framed as
   contracted commercial seizure under "letters of marque" issued by clients; the fiction
   contains no glorified lethal violence in the reporting period. Crews are adults; the
   historical "powder monkey" role is filled by adults. Pressing (forced recruitment) is a
   historical practice PSI abolished and reports as a remediated past impact. Negative S1
   impacts that remain (injuries, irregular pay, hazardous work) are reported honestly,
   because a demo tenant with only good news is useless.
8. **Vertical slices per ESRS topic.** Each CSRD task delivers facts + data + one sample
   pirate-speak answer for one topic, so any single slice can already be used in Salacia.
9. **Agent instructions live at the root.** `AGENTS.md` (with `CLAUDE.md` pointing to it)
   states the source-of-truth order, the style rules, and what to do when a fact is
   missing (propose it to canon, mark `[UNCHARTED]`, never silently invent).
10. **English only for the machine layer.** File names, YAML keys, CSV headers and
    frontmatter are plain English so tooling and agents are not fighting the voice.

## Repository layout (target)

```
README.md                          Entry point (short, standard English + one pirate-speak greeting)
AGENTS.md                          Instructions for agents working in or from this repo
CLAUDE.md                          One line: read AGENTS.md
canon/facts.yaml                   Single source of truth for numbers and names
canon/anachronisms.txt             Banned modern words/tech (one per line)
scripts/check_canon.py             Consistency checker (frontmatter, canon numbers, anachronisms, links)
brand/voice-and-language.md        Pirate-speak style guide, lexicon, CSRD glossary, the standard/pirate boundary
brand/brand-guidelines.md          Identity: flag, colours, type, naming, tone by audience
lore/research/real-pirate-practices.md   Sourced dossier of real pirate practice and how PSI uses it
lore/backstory.md                  1600s to today; timeline; the "stuck in time" rule
lore/bases.md                      The five bases
lore/fleet.md                      The 25 ships
lore/governance.md                 Council of Captains, roles mapped to modern equivalents
lore/people.md                     Named officers and key characters
lore/articles-of-agreement.md      The company code (share system, compensation, conduct)
lore/operations.md                 Routes, cargo, seasons, interdiction service, technology inventory
data/bases.csv                     Structured base register
data/fleet.csv                     Structured ship register
data/workforce.csv                 Headcount by entity/ship, role, gender, contract type
data/e1-activity-data.csv          Salacia-style activity data rows (entity, location, activity, quantity, unit, period)
data/iros.csv                      Double materiality impacts/risks/opportunities with scores
csrd/salacia-mapping.md            PSI ↔ Salacia organization, reporting year, entities, locations, products, roles
csrd/esrs2-general.md              ESRS 2: business model, value chain, strategy, governance, stakeholders
csrd/double-materiality.md         Assessment narrative, topics, thresholds, outcome
csrd/e1-climate.md                 Scope 1/2/3 story, base year, targets, transition plan
csrd/e2-e5-environment.md          Pollution, water, biodiversity, resource use
csrd/s1-workforce.md               Own workforce
csrd/s2-s4-value-chain-communities.md   Value-chain workers, communities, end users
csrd/g1-conduct.md                 Business conduct
agents/reporting-playbook.md       How to answer a datapoint / survey / DMA item in PSI's voice
agents/examples/*.md               Worked examples across topics and registers
tasks/plan.md, tasks/todo.md       This plan and its checklist
```

## Dependency graph

```
T1 canon + scaffold ─────┐
T2 checker script ───────┼──► T4 style guide ──► T10 brand guidelines
T3 pirate research ──────┘        │
        │                         │
        └──► T5 backstory ──► T6 bases ──► T7 fleet ──► T9 operations
                                │              │
                                └──► T8 governance/people/articles
                                                │
      T6+T7 ──► T11 Salacia mapping             │
      T8+T9 ──► T12 ESRS 2 general ──► T13 double materiality
                                          │
              ┌───────────┬───────────┬───┴───────┬───────────┐
            T14 E1      T15 E2–E5   T16 S1     T17 S2–S4   T18 G1
              └───────────┴───────────┴─────┬─────┴───────────┘
                                            ▼
                     T4+T11 ──► T19 AGENTS.md ──► T20 playbook ──► T21 examples ──► T22 dry run
```

Implementation order is bottom-up: canon and checker first (everything is verified
against them), research before any lore (so history informs invention), entities before
CSRD topics (topics quote entities), instructions last (they point at everything).

---

## Task list

### Phase 1 — Foundation

## Task 1: Repository scaffold and canon file

**Description:** Create the directory layout, a short `README.md`, and `canon/facts.yaml`
with every fact fixed by the brief plus the decisions that everything else depends on:
legal name and form, registered seat, founding year, fiscal year start month, reporting
year and base year, currency, fleet count, base count and region list, headcount band,
turnover band, CSRD scope justification (with the threshold values used). Take every
value from the decisions table at the end of this plan: N.V. seated in Vlissingen, founded
1621, start month 10, reported year `102024-092025`, base year `102023-092024`, EUR,
1,944 seagoing plus about 350 shore staff, about EUR 480M turnover, the five base towns
and the fleet mix by type. Verify the current CSRD thresholds (Omnibus) on the day and
record them with the date checked. Individual ship names and exact legal entity names are
left as explicit `TBD` placeholders to be filled by Tasks 6 and 7.

**Acceptance criteria:**
- [ ] `canon/facts.yaml` parses and contains every fact in the brief table above.
- [ ] Every row of the decisions table at the end of this plan has its value in canon; only ship names and exact entity names may be `TBD`.
- [ ] `README.md` explains what the repo is, in under 40 lines, and links to `AGENTS.md` (may not exist yet) and `tasks/plan.md`.

**Verification:**
- [ ] `uv run scripts/check_canon.py` exits 0 (PyYAML is resolved by uv from the script header; no system install).
- [ ] Manual check: directory tree matches the layout above (empty dirs may hold a `.gitkeep`).

**Dependencies:** None
**Files likely touched:** `README.md`, `canon/facts.yaml`, `canon/anachronisms.txt` (seed list), directory skeleton
**Estimated scope:** S

## Task 2: Consistency checker script

**Description:** Write `scripts/check_canon.py` (stdlib + PyYAML, run via `uv run` using inline script metadata) that walks the repo
and fails on: a Markdown file under `lore/`, `csrd/`, `brand/`, `agents/` without
frontmatter (`title`, `status`, `last-verified`, `canon-refs`); a numeric or named canon
fact quoted in prose that disagrees with `canon/facts.yaml` (checked via explicit
`{{canon.key}}`-style references or a per-file `canon-refs` list); any word from
`canon/anachronisms.txt` appearing outside code fences and outside an allowlisted
"out-of-character" block; a relative Markdown link that does not resolve; a CSV whose
header does not match its documented schema in the file's sibling `.schema.md`.

**Acceptance criteria:**
- [ ] Running the script on the Task 1 scaffold passes.
- [ ] Introducing one anachronism, one broken link and one wrong canon number each cause a non-zero exit with a file:line message.
- [ ] Script has a `--fix-frontmatter` dry-run-free helper that only reports, never edits.

**Verification:**
- [ ] `uv run scripts/check_canon.py` exits 0 on the clean scaffold.
- [ ] `uv run scripts/check_canon.py --self-test` runs the three negative cases against fixtures in `scripts/fixtures/` and exits 0.

**Dependencies:** Task 1
**Files likely touched:** `scripts/check_canon.py`, `scripts/fixtures/*`, `canon/anachronisms.txt`
**Estimated scope:** S

## Task 3: Research dossier on real pirate practice

**Description:** Research and write `lore/research/real-pirate-practices.md`: a sourced
dossier of what 17th- and early 18th-century pirates and privateers actually did, each
item with (a) what the sources say, (b) source links, (c) how PSI uses it, (d) what PSI
changes. Cover at minimum: articles of agreement and ship's codes (e.g. Bartholomew
Roberts, John Phillips); the share system and "no prey, no pay"; injury compensation
schedules recorded by Exquemelin; elected captains and the quartermaster's counterweight;
marooning and other discipline; careening and ship maintenance; provisioning (hardtack,
salt meat, grog, scurvy); navigation and gunnery of the period; letters of marque and the
privateer/pirate boundary; Dutch context (VOC and WIC, Piet Hein and the 1628 silver
fleet, the fluyt); bases and havens (Tortuga, Port Royal, Nassau's "republic of pirates",
Île Sainte-Marie and the Libertalia legend, Madagascar); Indian Ocean and Asian piracy
(Henry Every and the Ganj-i-Sawai, Kanhoji Angre, Iranun and Balangingi raiders of the
Sulu Sea, Zheng Yi Sao as a later reference); flags and signalling; the multi-ethnic and
occasionally female composition of crews; pressed men. Flag popular myths (walking the
plank, buried treasure maps) as myths. Also cover the "additional historical hooks" listed
in `tasks/decisions-open-questions.md` and confirm or tag as invented the two facts the
advisory could not verify (privateer bond sizes, the Admiralty's prize percentage).

**Acceptance criteria:**
- [ ] At least 15 practices, each with a source and a "how PSI uses it" line.
- [ ] A "myths" section separates fiction from record.
- [ ] A "period technology inventory" table lists what exists aboard a 1600s ship and what does not (the seed for `canon/anachronisms.txt`).

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes (frontmatter, links).
- [ ] Manual check: every source link opens; no claim without a source or an explicit "invented" tag.

**Dependencies:** Task 1 (may run in parallel with Task 2)
**Files likely touched:** `lore/research/real-pirate-practices.md`, `canon/anachronisms.txt`
**Estimated scope:** M

## Task 4: Pirate-speak style guide

**Description:** Write `brand/voice-and-language.md`: grammar and phonology rules
("be/ye/me/'tis", dropped g's, nautical metaphors), a core lexicon (100+ entries), a
CSRD glossary mapping standard terms to PSI terms and back (e.g. "double materiality
assessment" → "the reckonin' o' what matters", "Scope 1" stays "Scope 1"), the boundary
rule from architecture decision 2 as an explicit table (what is never translated), the
three registers with a side-by-side example of the same paragraph in each, a "do / don't"
list, and a short paragraph on avoiding caricature (no mock accents of real ethnic groups;
period authenticity from Task 3 over Hollywood).

**Acceptance criteria:**
- [ ] Glossary covers every ESRS topic name, the DMA vocabulary, and Salacia's core nouns (organization, legal entity, location, reporting year, activity data, emission factor, survey, evidence).
- [ ] The "never translated" table is present and matches architecture decision 2.
- [ ] Three-register example is present.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: an agent given only this file can rewrite a plain ESRS sentence into formal-register pirate speak with numbers intact (try three sentences).

**Dependencies:** Tasks 1, 3
**Files likely touched:** `brand/voice-and-language.md`, `canon/anachronisms.txt`
**Estimated scope:** S

## Task 5: Backstory and timeline

**Description:** Write `lore/backstory.md`: founding in the 1600s in the Dutch context,
the founding articles that froze technology, how the company survived four centuries
(havens, neutrality, contracts with whoever paid), its modern incorporation (why an EU
legal entity exists, so CSRD applies), how it grew to today's size, and why it now
reports sustainability at all (a client demanded it, an insurer demanded it, or the
Council decided the "reckonin'" is the new code — pick one and commit). Include a dated
timeline (20–30 entries) linking to the research dossier where a real event is borrowed.

**Acceptance criteria:**
- [ ] Every number quoted is a canon reference.
- [ ] The technology freeze is explained as a rule with consequences (what happens when a crew member brings a phone aboard).
- [ ] Timeline references at least 6 items from the research dossier.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: a reader can answer "why does a 17th-century company file a CSRD report?" from this file alone.

**Dependencies:** Tasks 1, 3
**Files likely touched:** `lore/backstory.md`, `canon/facts.yaml` (founding year, incorporation year if adjusted)
**Estimated scope:** S

### Checkpoint A — Foundation
- [ ] `uv run scripts/check_canon.py` and `--self-test` pass.
- [ ] Canon, research, style guide and backstory read as one consistent world.
- [ ] Human review of tone before entity work begins (voice is expensive to change later).

### Phase 2 — The company

## Task 6: The five bases

**Description:** Write `lore/bases.md` and `data/bases.csv` (+ `data/bases.schema.md`).
The five bases are decided: Vlissingen (seat, the home chamber), Baltimore in West Cork,
Port Royal in Jamaica, Île Sainte-Marie off Madagascar, and Ambon in the Moluccas; see the
decisions table for each one's historical hook and entity-name language. Each base: exact
legal entity name and form in the local language with an English gloss, function (shipyard, careening, warehouse,
counting house), headcount, year established, historical hook from the dossier, local
community and environment notes (feeds S3 and E4). Fill the base placeholders in canon.

**Acceptance criteria:**
- [ ] Exactly 5 bases; each maps to one legal entity in canon.
- [ ] CSV has one row per base with an ISO country code and coordinates.
- [ ] Each base has at least one community and one environmental note.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes (no remaining base `TBD` in canon).
- [ ] Manual check: headcounts across bases sum to the shore headcount in canon.

**Dependencies:** Task 5
**Files likely touched:** `lore/bases.md`, `data/bases.csv`, `data/bases.schema.md`, `canon/facts.yaml`
**Estimated scope:** M

## Task 7: The fleet

**Description:** Write `lore/fleet.md` and `data/fleet.csv` (+ schema). 25 ships in the
decided mix: 4 retourschepen (crew 220), 6 jachten (90), 8 fluyts (18), 5 interdiction
sloops or barks (70), 2 galjoots (15), totalling 1,944 seagoing crew. Per ship: name,
type, home base (chamber of enrolment), launch year, tonnage, crew size, guns, role
(cargo / interdiction / mixed), typical route, the crew's parten share, a one-line
character note. Ship names follow the naming convention (to be set here, referenced
by the brand guideline). Fill fleet placeholders in canon; ship crews must sum to the
seagoing headcount.

**Acceptance criteria:**
- [ ] Exactly 25 ships, each assigned to one of the 5 bases.
- [ ] Every ship type is period-appropriate (cross-checked with the dossier's technology inventory).
- [ ] CSV totals for crew match canon seagoing headcount.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] `python3 -c` one-liner summing the crew column equals the canon value.

**Dependencies:** Task 6
**Files likely touched:** `lore/fleet.md`, `data/fleet.csv`, `data/fleet.schema.md`, `canon/facts.yaml`
**Estimated scope:** M

## Task 8: Governance, people and the articles of agreement

**Description:** Write `lore/governance.md` using the decided two-tier structure: De
Heeren Vijf (supervisory, one bewindhebber per chamber, rotating presidency), the Raad van
Kapiteins (management board of elected captains under an elected Captain-General), the
Quartermaster-General (elected by all crews, keeper of the common chest, veto on
distributions, whistleblowing and sustainability officer), the Advocaat-Boekhouder
(secretary and chief bookkeeper), the Prize Council at Middelburg, and base Harbourmasters
as entity directors; a table mapping each to the modern role an auditor expects (CEO,
CFO, COO, supervisory board, audit committee, sustainability officer),
`lore/people.md` (8–12 named officers with a short bio each, diverse in origin as real
crews were), and `lore/articles-of-agreement.md` (the company code: shares and pay,
injury compensation schedule adapted from Exquemelin, voting, discipline, conduct toward
prizes and prisoners, the technology freeze, the reporting duty). The articles are a real
governance document the CSRD report will cite.

**Acceptance criteria:**
- [ ] Role-mapping table covers every governance body ESRS 2 GOV-1 to GOV-5 asks about.
- [ ] Articles contain the share system, compensation schedule, and the technology rule, each traceable to the dossier.
- [ ] People file names the signatories of the sustainability statement.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: no anachronistic titles (no "CEO" outside the mapping table).

**Dependencies:** Tasks 3, 6
**Files likely touched:** `lore/governance.md`, `lore/people.md`, `lore/articles-of-agreement.md`
**Estimated scope:** M

## Task 9: Operations

**Description:** Write `lore/operations.md`: trade routes between the seven regions with
seasonal constraints (monsoon, hurricane season, Roaring Forties), cargo categories with
example goods and why they are high-risk, the interdiction service written as the decided
five-step commission-to-condemnation procedure with the eight refusal conditions (final
wording set here), the share-based revenue model with the client / company / chamber /
crew split, and a period technology
inventory as used today (navigation, communication by packet ship and semaphore, record
keeping in ink on paper, how the annual report physically reaches the Salacia platform —
a scribe at a notary is fine).

**Acceptance criteria:**
- [ ] At least 6 named routes with season, duration, cargo and assigned ships.
- [ ] Interdiction service described including refusal conditions (architecture decision 7).
- [ ] Explains the paper-to-platform hand-off so the reporting story is coherent.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: every ship named appears in `data/fleet.csv`.

**Dependencies:** Task 7
**Files likely touched:** `lore/operations.md`
**Estimated scope:** S

## Task 10: Brand guidelines and visual identity

**Description:** Write `brand/brand-guidelines.md`: mission and promise in pirate speak,
the flag (described precisely enough to draw), colour palette named in period pigments
with modern hex values for designers, typography direction (blackletter or Dutch baroque
for display, a readable serif for body), logo description and usage rules, naming
conventions for ships, documents and bases, tone by audience (clients, crews, regulators,
port authorities), and examples of on-brand and off-brand copy. Optionally an SVG flag in
`brand/assets/`.

**Acceptance criteria:**
- [ ] Palette has at least 5 colours with pigment name, hex, and usage.
- [ ] Tone table covers the three registers from the style guide.
- [ ] Naming conventions agree with `data/fleet.csv` and `data/bases.csv`.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: the flag description can be reproduced by someone who has not read the lore.

**Dependencies:** Tasks 4, 5 (Task 7 for naming conventions)
**Files likely touched:** `brand/brand-guidelines.md`, `brand/assets/flag.svg` (optional)
**Estimated scope:** S

### Checkpoint B — The company
- [ ] Checker passes; no `TBD` remains in canon.
- [ ] Headcounts, ships and bases reconcile across canon, CSVs and prose.
- [ ] Human review: is the world fun, consistent and safe to publish as a demo?

### Phase 3 — CSRD knowledge base (one vertical slice per topic)

## Task 11: Salacia mapping

**Description:** Write `csrd/salacia-mapping.md`: how PSI is set up as a Salacia
organization: name, start month 10 and the resulting keys `102024-092025` (reported) and
`102023-092024` (base year), the root legal entity and one entity per base declared
for the reporting year, locations (each base and each ship as a location under its base's
entity), enabled products, who at PSI holds which Salacia role (E1 read & write, DMA,
survey respondent), and what evidence files a 17th-century company can attach (scanned
ledgers, logbook pages, notarised counts).

**Acceptance criteria:**
- [ ] Entity and location lists are generated from `data/bases.csv` and `data/fleet.csv` and match them exactly.
- [ ] Reporting-year key follows Salacia's period-key format.
- [ ] Role table names people from `lore/people.md`.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check against the Salacia domain-model note: every concept in the "What Salacia needs" table has a PSI answer.

**Dependencies:** Tasks 6, 7, 8
**Files likely touched:** `csrd/salacia-mapping.md`
**Estimated scope:** S

## Task 12: ESRS 2 general disclosures

**Description:** Write `csrd/esrs2-general.md` covering BP (basis for preparation,
consolidation scope, time horizons), GOV (bodies, sustainability skills, incentives, due
diligence, risk management — citing the articles), SBM (strategy, business model, value
chain map, stakeholders including port communities and clients, material IROs summary
placeholder filled by Task 13), and IRO-1 (the assessment process). Formal register.

**Acceptance criteria:**
- [ ] Every ESRS 2 disclosure requirement (BP-1 to IRO-2) has a section with facts, even if brief.
- [ ] Value chain map lists upstream (timber, hemp, sailcloth, tar, provisions), own operations, downstream (clients, buyers of goods).
- [ ] Numbers are canon references.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: an agent can fill a Salacia ESRS 2 narrative datapoint from this file without opening lore files.

**Dependencies:** Tasks 8, 9
**Files likely touched:** `csrd/esrs2-general.md`
**Estimated scope:** M

## Task 13: Double materiality assessment

**Description:** Write `csrd/double-materiality.md` and `data/iros.csv` (+ schema):
materiality topics (hierarchical, PSI's own wording mapped to ESRS topics), 20–30 IROs
each with type (impact +/−, risk, opportunity), value-chain position, time horizon,
scores on bounded criteria (scale, scope, irremediability, likelihood; magnitude for
financial), the thresholds used, and the outcome table stating which ESRS topics are
material and why (expect E1, E2, E4, E5, S1, S3, G1 material; E3 and S4 argued
immaterial or partially). Include the stakeholder engagement story (the parley).

**Acceptance criteria:**
- [ ] CSV rows carry all scoring fields and a topic mapping; scores are within the declared bounds.
- [ ] Outcome table lists every ESRS topic with material / not material and one-line rationale.
- [ ] Narrative explains the method in formal-register pirate speak.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: the material topics list equals the set of topic files planned in Tasks 14–18.

**Dependencies:** Task 12
**Files likely touched:** `csrd/double-materiality.md`, `data/iros.csv`, `data/iros.schema.md`
**Estimated scope:** M

## Task 14: E1 climate change

**Description:** Write `csrd/e1-climate.md` and `data/e1-activity-data.csv` (+ schema).
Scope 1 sources: galley firewood and charcoal, tar and pitch boiling at the yards,
gunpowder fired, whale oil and tallow for lamps and candles, livestock aboard. Scope 2:
zero, with the rationale that PSI buys no electricity, heat or steam (a fun and correct
zero; verify Salacia's location/market-based fields accept it). Scope 3: purchased goods
(timber, hemp, sailcloth, iron, provisions), capital goods (new hulls), upstream transport
(none: PSI is the transport), business travel (by packet ship), end-of-life of hulls
(scuttling, breaking). Base year, the reported year, transition plan ("we never had
engines; the plan is to keep it so and fix the tar kilns"), targets, and an energy mix
table (wind, muscle, biomass). Activity data rows per entity/location/period with units
Salacia's unit standardisation can resolve.

**Acceptance criteria:**
- [ ] Activity data CSV has ≥ 60 rows across all 5 entities and both years, with quantity, unit, period, activity type.
- [ ] Scope 1/2/3 narrative and target section exist; Scope 2 zero is justified.
- [ ] Every activity type names a plausible emission-factor category (wood, charcoal, tar/bitumen, explosives, animal fat).

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes; CSV validates against its schema.
- [ ] Manual check: totals per entity are sane relative to crew and ship counts (spot check two).

**Dependencies:** Tasks 7, 13
**Files likely touched:** `csrd/e1-climate.md`, `data/e1-activity-data.csv`, `data/e1-activity-data.schema.md`
**Estimated scope:** M

## Task 15: E2–E5 environment

**Description:** Write `csrd/e2-e5-environment.md`. E2 pollution: tar, pitch, lead shot,
bilge and ballast discharge, careening residues. E3 water: fresh-water casks, yard water
use, water stress at island bases. E4 biodiversity: oak and teak for hulls, careening on
reefs, exotic-materials sourcing (feathers, shells, hardwoods; what PSI refuses to carry),
invasive species via ballast and rats. E5 resource use: salvage and reuse of prize goods
and timbers, rope recycling into oakum, the near-total circularity of a wooden ship.
Metrics tables with canon-referenced numbers.

**Acceptance criteria:**
- [ ] Each of E2–E5 has policies, actions, targets and metrics sections (even if a target is "none set, because...").
- [ ] A refused-cargo list exists (protected species and materials).
- [ ] Metrics reference canon or `data/` files.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: nothing contradicts the E1 energy mix or the fleet register.

**Dependencies:** Task 13
**Files likely touched:** `csrd/e2-e5-environment.md`, `canon/facts.yaml` (metric values)
**Estimated scope:** S

## Task 16: S1 own workforce

**Description:** Write `csrd/s1-workforce.md` and `data/workforce.csv` (+ schema).
Headcount by entity, ship and shore, by gender and country of origin, contract type
(articled crew on shares vs waged shore staff), turnover, the share system as pay
structure and its living-wage problem ("no prey, no pay"), the injury compensation
schedule as the social protection scheme, health and safety incidents (falls from
rigging, scurvy cases, gunnery accidents), training (apprenticeship), collective voice
(crew votes, the quartermaster), grievance (the parley), and policies on forced and child
labour that record the abolition of pressing and the adults-only rule (architecture
decision 7). Include the ESRS S1 metric tables.

**Acceptance criteria:**
- [ ] Workforce CSV sums match canon total, seagoing and shore headcounts and the fleet crew totals.
- [ ] Incident and injury metrics for both years present.
- [ ] Pay narrative honestly reports the share-system risk and what PSI does about it.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes; CSV validates against schema.
- [ ] Manual check: gender and origin breakdowns are consistent with `lore/people.md` and the dossier's crew-composition findings.

**Dependencies:** Tasks 8, 13
**Files likely touched:** `csrd/s1-workforce.md`, `data/workforce.csv`, `data/workforce.schema.md`
**Estimated scope:** M

## Task 17: S2–S4 value chain, communities, end users

**Description:** Write `csrd/s2-s4-value-chain-communities.md`. S2: workers at
rope-walks, sawmills, sail lofts and provisioners; crews of the ships PSI interdicts (an
honest negative impact); dock labour at ports of call. S3: port communities at the five
bases and islands on the routes, indigenous communities near island bases, effects of
seizure on third-party trade. S4: buyers of the goods PSI delivers (spice merchants,
collectors) and PSI's clients for interdiction; argue partial materiality.

**Acceptance criteria:**
- [ ] Each topic has IRO summary, policies, engagement, remediation channels, targets.
- [ ] Interdicted crews are addressed explicitly, consistent with the refusal conditions in operations.
- [ ] Community notes match `lore/bases.md`.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: materiality conclusions match `csrd/double-materiality.md`.

**Dependencies:** Task 13
**Files likely touched:** `csrd/s2-s4-value-chain-communities.md`
**Estimated scope:** S

## Task 18: G1 business conduct

**Description:** Write `csrd/g1-conduct.md`: corporate culture (the articles), the
interdiction service as the central conduct question (client due diligence, letters of
marque, what is refused, how proceeds are booked), anti-corruption ("gifts to
harbourmasters" and how they are recorded and limited), whistleblowing (the parley and
the quartermaster's independence), supplier relationships and payment terms (paid in
shares of the voyage), political engagement (lobbying port authorities), and incidents
in the period with outcomes.

**Acceptance criteria:**
- [ ] Every G1 disclosure requirement has a section.
- [ ] Interdiction due-diligence procedure is written as a step list an auditor could test.
- [ ] Incident table for both years present.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: consistent with `lore/operations.md` and `lore/articles-of-agreement.md`.

**Dependencies:** Tasks 9, 13
**Files likely touched:** `csrd/g1-conduct.md`
**Estimated scope:** S

### Checkpoint C — CSRD knowledge base
- [ ] Checker passes.
- [ ] Every material topic from the DMA has a topic file; every topic file quotes canon.
- [ ] Human review: read one topic file cold and judge whether an auditor could follow it.

### Phase 4 — Agent enablement

## Task 19: Root agent instructions

**Description:** Write `AGENTS.md` (and a one-line `CLAUDE.md` pointing to it): what the
repo is, source-of-truth order (canon → data → csrd → lore → brand), the voice rules by
pointer to the style guide, the never-translate table restated, how to answer when a
fact is missing (mark `[UNCHARTED]`, propose a canon addition, never invent silently), the
requirement to run the checker before finishing, how to cite files in answers, what
registers to use for which output (Salacia narrative datapoint = formal, internal memo =
internal, press = marketing), and the ethical guardrails from architecture decision 7.

**Acceptance criteria:**
- [ ] Under 200 lines; every rule points to the file that holds the detail.
- [ ] Contains the missing-fact procedure and the checker command.
- [ ] `CLAUDE.md` exists and defers to `AGENTS.md`.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: a fresh agent session reading only `AGENTS.md` can locate the E1 Scope 1 figure within two file opens.

**Dependencies:** Tasks 4, 11
**Files likely touched:** `AGENTS.md`, `CLAUDE.md`
**Estimated scope:** S

## Task 20: Reporting playbook

**Description:** Write `agents/reporting-playbook.md`: step-by-step procedures for the
four things an agent will be asked to do for Salacia: (1) answer a narrative datapoint,
(2) provide a quantitative datapoint with unit and period, (3) fill or respond to a survey
assignment with evidence, (4) contribute to or explain the DMA. Each procedure: locate
facts → check canon → draft in the right register → keep identifiers standard → cite
sources → run checker. Include templates and a "common traps" list (translating units,
inventing ships, contradicting the materiality outcome).

**Acceptance criteria:**
- [ ] Four procedures with templates.
- [ ] Each template shows a filled example pointing at real repo files.
- [ ] Traps list has ≥ 8 entries drawn from things the checker cannot catch.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: follow procedure 2 by hand for one S1 metric and get the canon number.

**Dependencies:** Tasks 12–19
**Files likely touched:** `agents/reporting-playbook.md`
**Estimated scope:** S

## Task 21: Worked examples

**Description:** Write 5–6 examples in `agents/examples/`: an E1 narrative datapoint
(formal), an S1 quantitative table with commentary (formal), a DMA topic justification
(formal), a survey answer with an evidence description (formal/internal), an internal
memo from the Quartermaster-General to the Council (internal), and a client-facing
announcement (marketing). Each carries a header stating the register, source files and
canon refs used.

**Acceptance criteria:**
- [ ] All three registers represented; all numbers are canon references.
- [ ] Each example is under 400 words and cites its sources.
- [ ] No example contradicts a topic file.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: style guide "do / don't" list applied to each example; note fixes made.

**Dependencies:** Task 20
**Files likely touched:** `agents/examples/*.md`
**Estimated scope:** S

## Task 22: Dry run with a fresh agent

**Description:** Start a fresh agent session with only the repository, give it ten
representative Salacia requests (mixed narrative, quantitative, survey and DMA across at
least five topics), collect its answers, and score them for canon accuracy, register,
identifier hygiene, and citation. Record findings in `tasks/dry-run-1.md`, fix the
knowledge base gaps found, and re-run the failed items.

**Acceptance criteria:**
- [ ] 10 requests recorded with the answer and a pass/fail per criterion.
- [ ] Every failure traced to a repo fix (or an explicit "accepted") and re-tested.
- [ ] Final pass rate recorded.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes after fixes.
- [ ] Manual check: pass rate ≥ 9/10 on the re-run.

**Dependencies:** Task 21
**Files likely touched:** `tasks/dry-run-1.md`, plus whatever the fixes touch
**Estimated scope:** M

### Checkpoint D — Complete
- [ ] All acceptance criteria met; checker green.
- [ ] Dry run pass rate recorded.
- [ ] Ready for the first real Salacia reporting session on behalf of PSI.

---

## Parallelization

| Safe in parallel | Must be sequential | Needs a contract first |
| --- | --- | --- |
| T2 ‖ T3 (after T1) | T1 → everything | T6 fixes base names before T7, T11 |
| T8 ‖ T9 ‖ T10 (after T7) | T5 → T6 → T7 | T13 fixes the material topics before T14–T18 |
| T14 ‖ T15 ‖ T16 ‖ T17 ‖ T18 (after T13) | T19 → T20 → T21 → T22 | T4 fixes the never-translate table before any prose |

## Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Numbers drift between prose, CSVs and canon | High | Canon file + checker (T1, T2); CSV sums verified in T7, T16 |
| Anachronisms leak in (engines, radios, plastics, "email") | Med | `canon/anachronisms.txt` + checker; dossier technology inventory |
| Pirate speak mangles identifiers so Salacia cannot parse them | High | Never-translate table (T4) restated in AGENTS.md; examples show it |
| Voice becomes caricature or offensive | Med | Style-guide section on authenticity vs caricature; human review at Checkpoint A |
| Fiction glorifies violence, forced or child labour | High | Architecture decision 7 baked into articles, S1 and G1; human review at Checkpoint B |
| CSRD scope thresholds change again (Omnibus) | Low | Canon records the thresholds assumed and the date checked |
| Historical claims are wrong | Low | Dossier requires a source per claim; invented items tagged |
| Scope creep into building tooling or a website | Med | Only one script; anything else is a new plan |

## Decisions on the former open questions

Resolved on 2026-09-18 with an advisory agent briefed as a historian of 17th-century
piracy and Dutch maritime trade. Full grounding, rejected alternatives and sources are in
`tasks/decisions-open-questions.md`. Summary, binding for Task 1 onward:

| Question | Decision |
| --- | --- |
| Legal form and seat | Dutch N.V., seat Vlissingen; Prize Council and audit chamber in Middelburg; founded 1621 at the lapse of the Twelve Years' Truce; backstory explains the later re-incorporation as an N.V. |
| Fiscal year | 1 October to 30 September ("Kermis year"). Reported year FY2025 = Salacia key `102024-092025`; base year `102023-092024`; start month 10 |
| Reporting currency | EUR in every figure that reaches Salacia or a metric table; guilders of 20 stuivers only as a prose flavour column; pieces of eight and rijksdaalders only as cash-in-hand vocabulary |
| Ships as Salacia locations | Yes. Company-owned hulls, each enrolled at one chamber (base) and modelled as a location under that chamber's legal entity; crews hold a minority "parten" interest paid as the share |
| Interdiction framing | Five-step commission-to-condemnation procedure (registered letter of marque and bond, papers and crew examined, no breaking bulk, Prize Council adjudication, auction or ransom bill) with eight refusal conditions; no lethal violence in the reporting period |
| Headcount and turnover | 25 ships crewing 1,944 (4 retourschepen, 6 jachten, 8 fluyts, 5 interdiction sloops, 2 galjoots) plus about 350 shore staff, about 2,300 total; turnover about EUR 480M; Task 1 verifies the current Omnibus thresholds and records the date |
| Bases and entity-name languages | Vlissingen (Dutch), Baltimore in West Cork (English and Irish), Port Royal (English), Île Sainte-Marie (Malagasy and French), Ambon (Indonesian, PT form); each with an English gloss |
| Signatories | Captain-General for the Council of Captains and the presiding Lord of the Heeren Vijf, countersigned by the Quartermaster-General, figures attested by the Advocaat-Boekhouder |
