# Neederlandsch Schuijnvaerders Gilde — knowledge base

Ahoy. This repository is the single source of truth for the **Neederlandsch Schuijnvaerders
Gilde N.V.** (NSG, known in English-speaking ports as *Pirate Shipping Inc*): a fictitious
cargo and contracted-interdiction company that exists today, is large enough to fall under
the CSRD, and by its own articles uses nothing but the technology of a Dutch ship in the
1600s. Everything the company says, it says in pirate speak.

The knowledge base exists so that other agents can report on sustainability (ESRS under
CSRD) on the Gilde's behalf through the Salacia platform, consistently and in the right
voice.

## Where to start

- `AGENTS.md` — instructions for agents working in or from this repository (read first).
- `canon/facts.yaml` — every number and proper noun that must stay consistent.
- `brand/voice-and-language.md` — how the Gilde speaks, and what is never translated.
- `lore/` — backstory, bases, fleet, governance, people, articles, operations.
- `csrd/` — the ESRS knowledge base, one file per topic, plus the Salacia mapping.
- `data/` — structured registers (bases, fleet, workforce, activity data, materiality).
- `agents/` — the reporting playbook and worked examples.
- `tasks/plan.md` — the implementation plan; `tasks/decisions-open-questions.md` — decisions and their historical grounding.

## Checking consistency

```
uv run scripts/check_canon.py            # whole repository
uv run scripts/check_canon.py --self-test
```

Only `lore/research/real-pirate-practices.md`, this file and `AGENTS.md` are in plain
English; they record what is real and how to work. Everything else is in character.
