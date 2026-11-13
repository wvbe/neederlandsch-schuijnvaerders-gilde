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
port authorities), and examples of on-brand and off-brand copy.

**Acceptance criteria:**
- [ ] Palette has at least 5 colours with pigment name, hex, and usage.
- [ ] Tone table covers the three registers from the style guide.
- [ ] Naming conventions agree with `data/fleet.csv` and `data/bases.csv`.

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes.
- [ ] Manual check: the flag description can be reproduced by someone who has not read the lore.

**Dependencies:** Tasks 4, 5 (Task 7 for naming conventions)
**Files likely touched:** `brand/brand-guidelines.md`
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

---

# Phase 5 plan: policies, targets, actions and metrics

Planned 2026-11-13. Adds a set of standalone environment and relations policies, each with
the actions, targets and metrics ESRS asks for (MDR-P, MDR-A, MDR-T, MDR-M), to the knowledge
base built in Tasks 1–22. This is still a content repository. The only code change is one
line in the checker.

## Overview

Today the Gilde's standing orders, actions and targets sit inside the topic files (E1-2,
E2-1 … S4-5, G1-2, G1-5). They cover FY2025 and a single 2030 mark. Only E1 has a 2050 mark.
Phase 5 gives each material topic its own policy document under `policies/`. Each document
names its owner, scope, commitments, the actions planned for FY2026–FY2030, a target table
with annual milestones from FY2026 to FY2030 plus a 2050 mark, and the metric definitions
behind each target. An agent filling an E2-3 or S3-5 datapoint can then lift a whole MDR
answer from one file.

## Scope (decided with Wybe, 2026-11-13)

| Group | Policy file | ESRS | Builds on |
| --- | --- | --- | --- |
| Environment | `policies/e1-climate.md` | E1-2, E1-3, E1-4 | Vow of the Old Ways; galley-fuel and tar orders |
| Environment | `policies/e2-pollution.md` | E2-1, E2-2, E2-3 | Tar, lead-shot, bilge-and-ballast orders |
| Environment | `policies/e3-water-marine.md` | E3-1, E3-2, E3-3 | Water ration, high-stress chambers, no marine extraction |
| Environment | `policies/e4-biodiversity.md` | E4-2, E4-3, E4-4 | No reef careening, rats, oak planting, named timber sources |
| Environment | `policies/e5-resources.md` | E5-1, E5-2, E5-3 | Reuse of hull timber, rope and casks, landfill |
| Relations | `policies/s1-labour-relations.md` | S1-1, S1-2, S1-3, S1-4, S1-5, S1-8 | The articles, ships' councils, the parley |
| Relations | `policies/s2-value-chain-workers.md` | S2-1 … S2-5 | Sainte-Marie clause, chandler's undertaking, seized crews |
| Relations | `policies/s3-port-communities.md` | S3-1 … S3-5 | Port hearings, FPIC, port claims |
| Relations | `policies/s4-consignees-clients.md` | S4-1 … S4-5 | Honest manifest, provenance, auction origin statements |
| Relations | `policies/g1-supplier-relations.md` | G1-2, G1-6 | 30-day terms, shares of the voyage, chandlers' book |
| Relations | `policies/g1-political-engagement.md` | G1-5 | No political money, open petitions only |

Out of scope: S1 health and safety, pay and diversity (they stay in `csrd/s1-workforce.md`);
G1 anti-corruption and the commission due diligence; entering E1 targets into Salacia's
reduction plan (`backend-reduction-plan`). That last one is listed under open questions.

## Architecture decisions

- **Kermis years for the milestones.** Annual milestones are FY2026, FY2027, FY2028,
  FY2029 and FY2030 on canon's October–September year. The base year stays FY2024
  (`102023-092024`) and the 2050 mark is FY2050. The Salacia tenant's 2026 year is calendar
  `012026-122026`. That mismatch is not resolved here; it is listed under open questions.
- **FY2026 is a closed year.** It ended on 2026-09-30. Its milestone counts as set at the
  Kermis of 2025, before the year began, as the existing 2030 marks were. FY2026 actuals are
  `[UNCHARTED]` unless canon gains them. No policy invents an outcome for FY2026.
- **The existing 2030 marks do not move.** Each FY2030 milestone is the canon
  `target_2030_*` value that already exists. A policy that wants a different 2030 mark
  proposes the change in its canon proposal with a reason, and the Quartermaster-General
  decides.
- **Where numbers live.** New 2050 marks and any new headline metric go into canon in the
  topic block that already holds their 2030 sibling (`e1`, `environment`, `dma`, `g1`,
  `social_value_chain`). The year-by-year milestones go in a new register,
  `data/targets.csv`, one row per target, with its own `data/targets.schema.md`. Canon also
  gains a `policies:` block listing each policy: id, title, owning office, accountable
  office, adopted date, review cycle and file.
- **Canon first, through proposals.** Each drafting task writes its new numbers to
  `tasks/canon-proposals/policies-<id>.yaml` and its rows to
  `tasks/canon-proposals/policies-<id>.targets.csv`. One integration task per batch merges
  them into canon, `data/targets.csv` and the topic files. This lets the drafting tasks run
  in parallel even though E2–E5 share one canon block and one topic file, and so do S2–S4.
- **Gross targets, the Vow holds.** No target is met by offsets, credits or buying anything
  in. No action breaks `operations.technology_rule`. The 2050 marks must be reachable with
  17th-century means, which is why E1 does not claim net zero.
- **Six chambers from FY2026.** Vava'u opened in October 2025, so the scope of every policy
  from FY2026 covers 6 chambers (`company.chamber_count`). Vava'u has no baseline. Its
  per-chamber targets start from a baseline to be set in FY2026, and its unknown numbers
  stay `[UNCHARTED]`, as decision 9 requires.
- **One template.** Every policy file has the same sections, in the Formal register:
  frontmatter; purpose; scope (activities, value chain, chambers, hulls, exclusions);
  accountability (highest office answerable for it, and who carries it out day to day);
  commitments (the standing orders, quoted); third-party standards and stakeholders
  consulted; actions FY2026–FY2030 (what, where, when, resources, expected result);
  targets (a table of metric, unit, absolute or relative, base FY2024, FY2025, FY2026–FY2030,
  2050, scope); metrics (a definition, method, data source and canon key for each);
  monitoring and review (renewed at each Kermis); related files. The template lives in
  `policies/index.md`, and the E1 policy is the worked example of it.

## Dependency graph

```
T23 framework: canon policies block, data/targets.csv + schema, checker dir, policies/index.md
  │
  └── T24 E1 climate policy (pattern-setter)
        │
        ├── Checkpoint E: Wybe approves the template and target ambition
        │
        ├── T25 E2 ‖ T26 E3 ‖ T27 E4 ‖ T28 E5 ──► T29 integrate the environment batch
        │
        └── T30 S1 ‖ T31 S2 ‖ T32 S3 ‖ T33 S4 ‖ T34 G1-2 ‖ T35 G1-5 ──► T36 integrate the relations batch
                                                                          │
                                                   T29 + T36 ──► T37 Salacia mapping, playbook, DMA coverage
```

## Task list

### Phase 5a — Framework and pattern

## Task 23: Policy framework

**Description:** Lay the foundations every policy file stands on. Add the `policies:` block
to canon. Add the missing Scope 3 intensity marks to canon: `csrd/e1-climate.md` states 60
for 2030 and 45 for 2050, and canon has neither. Create `data/targets.csv` (header only)
with `data/targets.schema.md`. Add `policies` to `PROSE_DIRS` in `scripts/check_canon.py`
so the new folder gets checked. Write `policies/index.md`: the policy register, the
template, and the rules for setting targets (base year, Kermis milestones, 2050, gross).

**Acceptance criteria:**
- [ ] `canon/facts.yaml` has a `policies:` block with an entry for all 11 policies (files may not exist yet) and `e1.target_2030_scope3_intensity` = 60 and `e1.target_2050_scope3_intensity` = 45
- [ ] The `data/targets.csv` header and `data/targets.schema.md` agree. Columns include `policy_id`, `target_id`, `metric`, `unit`, `kind` (absolute or relative), `scope`, `base_fy2024`, `fy2025`, `fy2026` … `fy2030`, `fy2050`, `canon_key_2030`, `canon_key_2050`
- [ ] `policies/index.md` holds the register table, the section template and the target-setting rules, with frontmatter

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes and lists files under `policies/`
- [ ] Manual check: every row of the register points to a planned file name in the scope table above

**Dependencies:** None (Tasks 1–21 done)

**Files likely touched:** `canon/facts.yaml`, `data/targets.csv`, `data/targets.schema.md`,
`scripts/check_canon.py`, `policies/index.md`

**Estimated scope:** M

## Task 24: E1 climate policy (pattern-setter)

**Description:** Write `policies/e1-climate.md` to the template, from the Vow of the Old
Ways and the two standing orders. Planned actions FY2026–FY2030: kiln hoods at Vava'u,
charcoal in every galley that can carry it, pressed lamp oil across all chambers, and a
sail-plan log. Targets: fossil Scope 1, Scope 3 intensity and the renewable energy share,
each with FY2026–FY2030 milestones and a 2050 mark. Merge this task's canon additions and
targets rows directly, without a proposal file, so the integration pattern is proven once.
Point the E1-2, E1-3 and E1-4 sections of `csrd/e1-climate.md` to the policy.

**Acceptance criteria:**
- [ ] Every template section is present. The FY2030 and 2050 values equal canon (`e1.target_2030_scope1_tco2e`, `e1.target_2050_scope1_tco2e` and the Task 23 intensity keys)
- [ ] The Scope 1 milestones fall every year from FY2025 (168.0) to FY2030 (110). Each action states the chamber or hull class, the year and the resource
- [ ] `data/targets.csv` has the E1 rows, and `csrd/e1-climate.md` links to the policy without repeating its tables

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes
- [ ] Manual check: the Formal register follows `brand/voice-and-language.md`, and numbers, units and ESRS codes are untranslated

**Dependencies:** T23

**Files likely touched:** `policies/e1-climate.md`, `canon/facts.yaml`, `data/targets.csv`,
`csrd/e1-climate.md`

**Estimated scope:** M

### Checkpoint E — Pattern approved
- [ ] Checker passes
- [ ] Wybe reads `policies/e1-climate.md`, approves the template and target ambition, or asks for changes before the fan-out

### Phase 5b — Environment policies (T25–T28 in parallel)

Each of T25–T28 follows the same shape, so it is written out once here.

**Description (shared):** Write the policy file to the template, built on the standing
orders already in the matching section of `csrd/e2-e5-environment.md`. Propose
FY2026–FY2029 milestones that run toward the existing 2030 mark, a 2050 mark for every
target, and any new metric the policy needs, with a FY2024 and FY2025 value consistent with
the activity data. Write the numbers to the task's canon-proposal YAML and the rows to its
targets fragment. Do not edit canon, `data/targets.csv` or the topic file; that is T29.

**Acceptance criteria (shared):**
- [ ] All template sections present. Each target has a base, FY2025, five milestones and a 2050 mark, and each FY2030 equals the existing canon 2030 key
- [ ] Every number in the policy is either already in canon or in the task's proposal YAML, with a one-line reason
- [ ] No action or 2050 mark breaks `operations.technology_rule`. Vava'u appears in scope, with uncharted values marked `[UNCHARTED]`

**Verification (shared):**
- [ ] `uv run scripts/check_canon.py` passes. Canon-ref warnings for keys still in proposal are expected and listed in the task's hand-off note
- [ ] Manual check: each milestone series moves monotonically from FY2025 toward FY2030

**Dependencies (shared):** Checkpoint E

**Estimated scope (each):** S, 3 files

## Task 25: E2 pollution policy
Targets: tar boiled, kiln volatile losses, lead shot recovered, scrapings landed, discharges
within a league, white-lead paint. The 2050 marks to propose include whether lead shot is
fired over water at all.
Files: `policies/e2-pollution.md`, `tasks/canon-proposals/policies-e2.yaml`, `tasks/canon-proposals/policies-e2.targets.csv`

## Task 26: E3 water and marine resources policy
Targets: water drawn at the high-stress chambers, rainwater share of island-yard water, and
`marine_resources_extracted: none` kept as a standing commitment.
Files: `policies/e3-water-marine.md`, `tasks/canon-proposals/policies-e3.yaml`, `tasks/canon-proposals/policies-e3.targets.csv`

## Task 27: E4 biodiversity policy
Targets: no reef careening, rat incidents, oak planted per year, named replanted timber
source. Takes in the E4-1 transition plan and the hard surveys, with a signed hard survey
for Vava'u in FY2026.
Files: `policies/e4-biodiversity.md`, `tasks/canon-proposals/policies-e4.yaml`, `tasks/canon-proposals/policies-e4.targets.csv`

## Task 28: E5 resource use and circularity policy
Targets: reused share of inflow (with and without provisions), broken hull timber reused,
landfill share.
Files: `policies/e5-resources.md`, `tasks/canon-proposals/policies-e5.yaml`, `tasks/canon-proposals/policies-e5.targets.csv`

## Task 29: Integrate the environment batch

**Description:** Bring T25–T28 in once Wybe, as Quartermaster-General, has approved the
proposals. Merge the four YAMLs into the `environment` canon block, append the fragments to
`data/targets.csv`, add `canon-refs` to the policy frontmatter, and point E2-1/E2-3,
E3-1/E3-3, E4-2/E4-4 and E5-1/E5-3 in `csrd/e2-e5-environment.md` to the policies. Then
delete the merged proposal files, or mark them merged as earlier tasks did.

**Acceptance criteria:**
- [ ] No proposal key is left unmerged without a written reason. `data/targets.csv` holds the E1–E5 rows
- [ ] Each FY2030 and FY2050 cell in `data/targets.csv` equals its canon key

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes with no canon-ref warnings
- [ ] Manual check: a short script or a read-through compares the CSV 2030/2050 columns with canon

**Dependencies:** T25–T28

**Files likely touched:** `canon/facts.yaml`, `data/targets.csv`, `csrd/e2-e5-environment.md`,
the four policy files

**Estimated scope:** M

### Checkpoint F — Environment complete
- [ ] Checker passes; five environment policies are live and linked

### Phase 5c — Relations policies (T30–T35 in parallel)

Same shared description, acceptance criteria and verification as Phase 5b. Relations
targets often have no 2030 key yet; where none exists, the task proposes one. Guardrails
from `AGENTS.md` section 5 apply in full. Dependencies: Checkpoint E (not F; the two
batches are independent).

## Task 30: S1 labour relations policy
Covers the articles as the collective instrument, ships' councils, election and removal of
officers, the parley and appeal times, and the stated lack of an external representative
body. Targets to propose: parley cases closed within the appeal window, hands at the Kermis
vote, and a step toward an external representative body by 2050 (or a reasoned refusal).
The existing S1-5 marks (hurts, women, floor payment) are referenced, not restated.
Files: `policies/s1-labour-relations.md`, `tasks/canon-proposals/policies-s1.yaml`, `tasks/canon-proposals/policies-s1.targets.csv`

## Task 31: S2 value-chain workers policy
Builds on the existing 2027 marks: supplier visits, two-year coverage, the rope-walk code,
and seized-crew complaints closed within 30 days. Extends them to FY2030 and 2050, and keeps
"no forced or child labour finding" as a yearly zero.
Files: `policies/s2-value-chain-workers.md`, `tasks/canon-proposals/policies-s2.yaml`, `tasks/canon-proposals/policies-s2.targets.csv`

## Task 32: S3 port communities policy
Port hearings per chamber (now 6), FPIC, port claims and closure days, and Vlissingen tar
smoke claims (the 2028 mark).
Files: `policies/s3-port-communities.md`, `tasks/canon-proposals/policies-s3.yaml`, `tasks/canon-proposals/policies-s3.targets.csv`

## Task 33: S4 consignees and clients policy
Honest manifest, provenance papers travelling with the parcel, auction origin statements,
the tortoiseshell standing order, and complaint closure. Targets are newly proposed, since
S4 has none in canon.
Files: `policies/s4-consignees-clients.md`, `tasks/canon-proposals/policies-s4.yaml`, `tasks/canon-proposals/policies-s4.targets.csv`

## Task 34: G1 supplier relations and payment policy
30-day terms, shares of the voyage, invoices within terms, average days to pay, and conflict
of interest at the Harbourmaster's desk. **Must reconcile** `g1.supplier_count_fy2025` (96)
with `social_value_chain.suppliers_on_register_fy2025` (63). The likely reading is that the
chandlers' book is a subset of all suppliers; state it, or propose a canon fix.
Files: `policies/g1-supplier-relations.md`, `tasks/canon-proposals/policies-g1-2.yaml`, `tasks/canon-proposals/policies-g1-2.targets.csv`

## Task 35: G1 political engagement policy
No political money, petitions only, in the open and on the public record, and an entry
in a transparency register before any lobbying begins. Targets: EUR 0 every year and
petitions published within a set number of days. 2050 restates the commitment.
Files: `policies/g1-political-engagement.md`, `tasks/canon-proposals/policies-g1-5.yaml`, `tasks/canon-proposals/policies-g1-5.targets.csv`

## Task 36: Integrate the relations batch

**Description:** The same procedure as T29, for T30–T35. Merge into the `dma`,
`social_value_chain` and `g1` blocks, append to `data/targets.csv`, and link from
`csrd/s1-workforce.md`, `csrd/s2-s4-value-chain-communities.md` and `csrd/g1-conduct.md`.

**Acceptance criteria / verification:** As T29, for the relations rows.

**Dependencies:** T30–T35

**Estimated scope:** M

### Phase 5d — Wiring

## Task 37: Salacia mapping, playbook and DMA coverage

**Description:** Make the policies findable and complete. Add the policy files to
`csrd/salacia-mapping.md` against each datapoint they answer. Add a "policy, action or
target datapoint" route to `agents/reporting-playbook.md`. Check every material IRO in
`data/iros.csv` against a policy. ESRS requires the report to say so when a material topic
has no policy, so either name the policy or record why there is none.

**Acceptance criteria:**
- [ ] Each of the 11 policies appears in the mapping with its datapoint codes
- [ ] The playbook names `policies/` and `data/targets.csv` as the source for MDR-P/A/T/M answers
- [ ] Every material IRO maps to a policy or has a stated reason in its topic file

**Verification:**
- [ ] `uv run scripts/check_canon.py` passes (the one run for the phase, per the lean-validation preference)

**Dependencies:** T29, T36

**Files likely touched:** `csrd/salacia-mapping.md`, `agents/reporting-playbook.md`,
`policies/index.md`, possibly a topic file

**Estimated scope:** S

### Checkpoint G — Phase 5 complete
- [ ] Checker green
- [ ] Eleven policies, each with actions, a FY2026–FY2030 trajectory, a 2050 mark and defined metrics
- [ ] Wybe signs off as Quartermaster-General

## Parallelization (Phase 5)

- Sequential: T23 → T24 → Checkpoint E.
- Then two independent lanes: T25–T28 in parallel, then T29; and T30–T35 in parallel, then T36.
  Up to ten drafting agents can run at once. Each writes only its own policy file and its
  own proposal files, so they never collide. Agents run on Opus, per Wybe's preference.
- T37 last.

## Risks and mitigations (Phase 5)

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Parallel drafts collide in shared canon blocks and topic files | High | Drafting tasks write proposal files only; one integration task per batch |
| Targets drift from the existing 2030 marks | Med | FY2030 must equal the existing canon key; changes only by proposal with a reason |
| 2050 marks that need modern technology | Med | Each 2050 mark checked against `operations.technology_rule` in acceptance criteria |
| Invented FY2026 actuals | Med | FY2026 actuals are `[UNCHARTED]`; only the milestone is stated |
| Vava'u numbers invented to fill a per-chamber target | Med | Baseline "to be set in FY2026"; unknowns stay `[UNCHARTED]` (decision 9) |
| Supplier count mismatch (96 vs 63) leaks into two policies | Low | T34 reconciles it; T31 cites T34's resolution at integration |
| The policies repeat the topic files and the two drift apart | Med | Topic files keep FY2025 facts and link to the policy for the forward-looking part; tables are not duplicated |

## Open questions (Phase 5)

- **Calendar mismatch.** Canon's Kermis year against the tenant's calendar
  `012026-122026`. These milestones use Kermis years. If the tenant stays on calendar years,
  a separate decision is needed on how an FY2027 milestone is reported in calendar 2027.
- **Salacia reduction plan.** Should the E1 targets and the FY2026–FY2030 pathway also be
  entered into the tenant's reduction plan (targets, pathways, projects), or stay in the
  narrative datapoints only? This is a later, separate task.
- **2050 ambition for relations topics.** Many relations 2050 marks will restate a standing
  commitment, such as "zero findings" or "EUR 0". Is that acceptable, or should each have a
  measurable stretch mark?
