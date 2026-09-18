# Instructions for agents working in or from this repository

This repository is the knowledge base of the **Neederlandsch Schuijnvaerders Gilde N.V.**
(NSG, English trade name *Pirate Shipping Inc*), a fictitious company that reports on
sustainability under the CSRD through the Salacia platform. You are either extending the
knowledge base or using it to answer on the Gilde's behalf. Both jobs follow the rules
below. This file is written in plain English on purpose; almost everything else here is in
the Gilde's voice.

## 1. Source-of-truth order

When two files disagree, the earlier one in this list wins, and the later one is the bug:

1. `canon/facts.yaml` — every number and proper noun. If it is not in canon, it is not a fact.
2. `data/*.csv` — structured registers (bases, fleet, workforce, activity data, IROs). Each has a sibling `*.schema.md`.
3. `csrd/*.md` — the ESRS knowledge base, one file per topic, plus `csrd/salacia-mapping.md`.
4. `lore/*.md` — backstory, bases, fleet, governance, people, articles, operations.
5. `brand/*.md` — voice, language, identity.
6. `lore/research/real-pirate-practices.md` — what is historically real; the lore may bend it only where that file says so.

`tasks/plan.md` and `tasks/decisions-open-questions.md` explain why things are as they are.
They are planning records, not facts about the company.

## 2. Voice

Every word the Gilde says is pirate speak, in one of three registers defined in
`brand/voice-and-language.md`. Read that file before writing anything in character. Use:

| Output | Register |
| --- | --- |
| Salacia narrative datapoint, sustainability statement, policy, letter to a regulator or auditor | Formal |
| Survey answer for the Quartermaster, logbook, memo between officers, articles | Internal |
| Client announcement, recruitment, press, the brand book | Marketing |

## 3. What is never translated

Numbers, units, currency codes (EUR), ISO dates, Salacia period keys (`102024-092025`),
ESRS codes and datapoint names (E1-6, GOV-1), legal entity names, place names, ISO country
codes, people's names and titles of office, Scope 1/2/3, quoted law, and all YAML keys,
CSV headers, table header rows, frontmatter and file names. The full table is section 1 of
`brand/voice-and-language.md`. If a token is machine-readable, leave it alone.

## 4. When a fact is missing

Do not invent it silently. In order of preference:

1. Look again: canon, then the data files, then the topic file, then the lore.
2. If it is genuinely absent, write `[UNCHARTED]` in place of the value, say in one sentence
   what is missing, and propose a canon addition (key, value, one-line rationale) at the end
   of your answer or in `tasks/canon-proposals.md`.
3. Never resolve an `[UNCHARTED]` by picking a plausible number. The Quartermaster-General
   (a human) decides what enters canon.

The same applies to ships, bases, people and events: if it is not in `data/fleet.csv`,
`data/bases.csv`, `lore/people.md` or `lore/backstory.md`, it does not exist.

## 5. Ethical guardrails baked into the fiction

These are not optional flavour; they are canon and they bound what you may write:

- Every hand is an adult. There is no child labour, and the historical "powder monkey" role is filled by adults.
- Pressing (forced recruitment) was abolished and is reported as a remediated historical impact. No forced labour in the reporting period.
- The interdiction business is contracted commercial seizure under a client's letter of marque, following the five-step commission-to-condemnation procedure in `lore/operations.md`, with its eight refusal conditions. No lethal violence occurs in the reporting period. Casualties belong to history, not to the reported year.
- The voice is a house style, not an imitation of any real people or accent. No mock accents of real ethnic groups; no jokes resting on one.
- Bad news is reported first and plainly. The voice never hides an injury, an incident or a missed target.

## 6. Before you finish

Run the checker from the repository root and fix what it reports:

```
uv run scripts/check_canon.py
```

It verifies frontmatter, canon references, anachronisms, numeric guards, relative links
and CSV headers. `uv` resolves PyYAML from the script header; nothing needs installing. A
new prose file under `brand/`, `lore/`, `csrd/` or `agents/` needs frontmatter with
`title`, `status`, `last-verified` and `canon-refs`. A word from
`canon/anachronisms.txt` may be used only when the standard requires it, allowed per file
with `allow-anachronisms:` and a reason.

## 7. Citing

When you answer on the Gilde's behalf, name the files the answer rests on, as repository
paths, at the end of the answer or in the evidence field. Canon keys are the most precise
citation: `scale.seagoing_headcount` beats "the headcount file".

## 8. How to answer a Salacia request

The step-by-step procedures for narrative datapoints, quantitative datapoints, survey
assignments and the double materiality assessment, with templates and worked examples, are
in `agents/reporting-playbook.md` and `agents/examples/`. Read the playbook once, then
follow the procedure that matches the request.

## 9. Editing this repository

- Change canon first, prose second. Never leave a number in prose that canon does not hold.
- Keep the machine layer in plain English and lower case.
- Keep `lore/research/real-pirate-practices.md`, `README.md` and this file in plain English; everything else in character.
- Do not add tooling beyond the one checker without a plan in `tasks/`.
- Tick `tasks/todo.md` only when a task's acceptance criteria and verification in `tasks/plan.md` are met.
