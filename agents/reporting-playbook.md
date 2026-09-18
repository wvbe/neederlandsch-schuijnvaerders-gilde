---
title: The Reportin' Playbook — how an agent answers for the Gilde
status: draft
last-verified: 2026-09-18
canon-refs: [reporting.reported_year_key, reporting.base_year_key, e1.scope1_fossil_tco2e_fy2025, e1.scope2_tco2e, governance.injury_schedule_eur.right_arm, scale.fleet_count]
---

# The Reportin' Playbook — how an agent answers for the Gilde

Ye be about to speak for the Neederlandsch Schuijnvaerders Gilde on the Salacia platform.
Four kinds o' request come: a narrative datapoint, a quantitative datapoint, a survey
assignment, an' a question about the reckonin' o' what matters (the double materiality
assessment). Each has its procedure below. All four share the same spine: **find the fact,
check it against canon, write it in the right register, keep the machine layer standard,
cite the file, run the checker.** Read `../AGENTS.md` once afore ye start; it holds the
rules this playbook applies.

## 0. The spine

| Step | What ye do | Where |
| --- | --- | --- |
| Find | Locate the fact in the topic file for the ESRS code asked | `../csrd/` |
| Check | Confirm every number an' name against canon or a `data/` register | `../canon/facts.yaml`, `../data/` |
| Register | Formal for anythin' a regulator sees; internal for a survey answer to the Quartermaster | `../brand/voice-and-language.md` §2 |
| Boundary | Numbers, units, dates, period keys, ESRS codes, entity names, hull names stay standard | `../brand/voice-and-language.md` §1 |
| Cite | Name the repository files an' canon keys the answer rests on | this file, §6 |
| Check again | `uv run scripts/check_canon.py` if ye wrote into the repository | `../scripts/` |

Where the fact be absent, write `[UNCHARTED]`, say what be missing in one sentence, an'
propose a canon key. Never fill the gap with a likely number.

## 1. A narrative datapoint

The platform asks, for a disclosure requirement (say E1-1 or GOV-2), for prose.

**Procedure**
1. Open the topic file whose name matches the code: E1 → `../csrd/e1-climate.md`; E2 to E5 → `../csrd/e2-e5-environment.md`; S1 → `../csrd/s1-workforce.md`; S2 to S4 → `../csrd/s2-s4-value-chain-communities.md`; G1 → `../csrd/g1-conduct.md`; BP, GOV, SBM, IRO → `../csrd/esrs2-general.md`.
2. Read the section headed with that code. Lift its facts; do not paraphrase a number.
3. If the section points to lore (the articles, the backstory, operations), read that too, but quote only what the topic file needs.
4. Draft one to four paragraphs in the **formal register**. Give the standard term in brackets at first mention. No headings inside the datapoint. Bad news first.
5. Check each number against canon. Check each name against `../data/fleet.csv`, `../data/bases.csv`, `../lore/people.md`.
6. Append the citation line.

**Template**

```text
<Paragraph 1: the answer, bad news first, standard term in brackets at first mention.>
<Paragraph 2–4: the facts the requirement asks for, each number as canon writes it.>

Sources: csrd/<topic>.md §<code>; canon: <key>, <key>; data/<file>.csv
```

**Filled example (E1-6, Scope 1 an' 2, period 102024-092025)**

```text
In the Kermis year 102024-092025 the Gilde's own smoke (Scope 1 greenhouse gas emissions)
came to 168.0 tCO2e, down from 185.9 tCO2e in the year we measure from, 102023-092024. It
arises from the tar an' pitch boiled at our careenin' hards, the whale oil an' tallow burned
for light, the black powder fired for signals an' exercise, an' the livestock carried for
the table. Smoke from firewood an' charcoal in the galleys, bein' biogenic, be reported
separately an' not in this figure.

Smoke bought in (Scope 2) be 0 tCO2e on both the location-based an' the market-based
measure, for the Gilde buys no electricity, heat or steam at any chamber or aboard any of
its fleet of 25 wooden ships; its articles forbid the gear that would use them. The
figures be computed on the platform from the activity data in the boekhouder's ledgers
an' the gunner's books, matched to the emission factors set out in E1-6.

Sources: csrd/e1-climate.md §E1-6; canon: e1.scope1_fossil_tco2e_fy2025,
e1.scope1_fossil_tco2e_fy2024, e1.scope2_tco2e; data/e1-activity-data.csv
```

## 2. A quantitative datapoint

The platform asks for a number with a unit for a period.

**Procedure**
1. Find the number in canon first (`../canon/facts.yaml`). If canon lacks it, find it in the `data/` register or the topic file's metric table; if it be there an' not in canon, answer it **an'** propose the canon key.
2. Confirm the unit be the one the standard names (tCO2e, MWh, m³, t, EUR, headcount, %, hours).
3. Confirm the period key: `102024-092025` for the reckonin', `102023-092024` for the year measured from.
4. Write the number, the unit, the period key an' one sentence o' formal register namin' the source document (ledger, muster roll, gunner's book, careenin' record, commissie register).
5. Never round in the answer what canon holds unrounded.

**Template**

```text
<value> <unit> — period <key>
<One sentence, formal register, naming the source document and the file.>
Sources: canon: <key>; <file>
```

**Filled example (S1-11, social protection: compensation for loss o' the right arm)**

```text
EUR 60,000 — period 102024-092025
'Tis the sum the Matanzas schedule (1628, restated in EUR) pays from the common chest to any
hand who loses the right arm in the Gilde's service, as fixed in the articles an' paid
within a month o' the surgeon's report.
Sources: canon: governance.injury_schedule_eur.right_arm; lore/articles-of-agreement.md;
csrd/s1-workforce.md §S1-11
```

## 3. A survey assignment

The platform issues a survey (a *muster o' questions*) to a location — a chamber or a hull
— an' asks the master or Harbourmaster to answer, with evidence.

**Procedure**
1. Identify the location an' its legal entity from `../csrd/salacia-mapping.md` §3. Answer as that location's officer (the Harbourmaster for a chamber, the master for a hull, named in `../lore/people.md` where a name be needed).
2. For each question, find the fact in the topic file or the `data/` register **for that location only**. A hull's galley wood be her row in `../data/e1-activity-data.csv`; her hands be her rows in `../data/workforce.csv`.
3. Write in the **internal register** (a logbook voice) unless the survey says the regulator will read it, in which case formal.
4. Name the evidence from the evidence table in `../csrd/salacia-mapping.md` §6: ledger page, logbook leaf, gunner's book, muster roll, Matanzas ledger, commissie register, notary's count, careenin' record. Describe the page ye would attach: which book, which chamber, which dates.
5. If a question asks for somethin' a 1600s company cannot have (a meter readin', a licence number for gear it does not own), answer plainly that the Gilde has none an' why, in one sentence, an' cite the Vow of the Old Ways.

**Template**

```text
Location: <hull or chamber> — Legal entity: <exact entity name> — Period: <key>
Answered by: <office>, <name>

Q<n>. <question>
A. <answer, internal register, numbers standard>
Evidence: <book>, <chamber or hull>, <date range>; file: data/<file>.csv rows for <location>

Sources: csrd/salacia-mapping.md §3, §6; <topic file>; canon: <keys>
```

**Filled example (fluyt *Gheduld*, NSG-11, galley fuel question)**

```text
Location: Gheduld (NSG-11) — Legal entity: Neederlandsch Schuijnvaerders Gilde N.V. — Period: 102024-092025
Answered by: Harbourmaster, Kamer Vlissingen

Q3. State the fuel burned aboard in the period, by kind an' quantity.
A. Firewood for the galley, as tallied in the boekhouder's ledger for the hull, an' a lesser
measure o' charcoal for the long southern passages. No oil, no coal, no other fuel: the
Gheduld be a fluyt o' 18 hands an' carries no gear that would burn it. Quantities be as the
platform holds them from the ledger rows for this hull; I have read them back against the
ledger an' they agree.
Evidence: boekhouder's ledger, Kamer Vlissingen, 1 October 2024 to 30 September 2025, the
Gheduld's page; file: data/e1-activity-data.csv rows where location = Gheduld

Sources: csrd/salacia-mapping.md §3, §6; csrd/e1-climate.md §Method an' evidence;
data/fleet.csv (NSG-11)
```

## 4. The reckonin' o' what matters (double materiality)

The platform asks ye to explain, defend or extend the assessment.

**Procedure**
1. The method, the thresholds, the topics an' the outcome be in `../csrd/double-materiality.md`; the scored IROs be in `../data/iros.csv`. Read both afore answerin' anythin'.
2. To explain why a topic be material, quote its IRO rows (by `iro_id`), their scores an' the threshold. Never re-score in the answer.
3. To answer "is X material", find X in the outcome table. If X be not there, it was not assessed: say so, an' propose it as a new IRO for the Quartermaster-General's next Kermis parley, with the scores ye would give an' why, clearly marked as a proposal.
4. Keep the DMA vocabulary as the glossary maps it: *the reckonin' o' what matters* (double materiality assessment), *our wake* (impacts), *our weather* (risks), *our fair winds* (opportunities), *a matter that weighs* (material topic). ESRS topic codes stay standard.
5. Formal register always; the Quartermaster-General owns this assessment an' speaks in the Council's voice.

**Template**

```text
Topic: <ESRS code an' the Gilde's name for it> — Outcome: material / partially material / not material
Why: <one paragraph quoting the IRO ids, scores an' the threshold>
IROs: <IRO-xx (type, score)>, ...
Sources: csrd/double-materiality.md §The outcome; data/iros.csv; canon: dma.*
```

## 5. Common traps the checker cannot catch

1. **Translatin' a unit or a code.** "Scope 1" stays "Scope 1"; "tCO2e" stays "tCO2e". The checker sees words, not meanin'.
2. **Roundin' in prose what canon holds exact.** 2,294 be 2,294 in a datapoint; "about 2,300" be for speech.
3. **Inventin' a hull, a chamber or an officer** that reads plausible. Only `data/fleet.csv`, `data/bases.csv` an' `lore/people.md` exist.
4. **Answerin' for the wrong period.** The reckonin' be `102024-092025`; the year measured from be `102023-092024`. A calendar year be never right.
5. **Contradictin' the materiality outcome** — callin' a topic material in a narrative that the DMA marked partial, or the reverse.
6. **Lettin' the voice bury bad news.** If the number went the wrong way (as the Scope 3 intensity did in FY2025), the first sentence says so.
7. **Usin' the marketing register for a regulator.** Swagger be for clients. A datapoint be formal.
8. **Puttin' pirate speak in a table header, a key or a file name.** The machine layer stays plain English.
9. **Claimin' evidence the Gilde cannot hold** — a meter, a licence for gear it does not own, a wire. Evidence be ink on paper, listed in the mappin'.
10. **Fillin' an `[UNCHARTED]` with a likely number.** Propose it; do not assert it.
11. **Quotin' the guilder column as a value.** Guilders be flavour in prose tables only; every reported figure be EUR.
12. **Treatin' the seized crews as anythin' but an actual negative impact.** The articles protect them; the reckonin' still calls the seizure what it be.

## 6. How to cite

End every answer with a `Sources:` line namin' repository paths an' canon keys, most
precise first: canon key, then `data/` file, then the topic file an' section, then lore.
Canon keys be written as dotted paths (`e1.scope1_fossil_tco2e_fy2025`). A section be
named by its ESRS code (`§E1-6`) or its heading.

## Related

- [Worked examples](examples/) — one per register an' request kind
- [Agent instructions](../AGENTS.md)
- [Voice an' language](../brand/voice-and-language.md)
- [The Salacia mappin'](../csrd/salacia-mapping.md)
- [Canon](../canon/facts.yaml)
