# Todo: Pirate Shipping Inc knowledge base

Checklist companion to `tasks/plan.md`. Decisions on the former open questions are in `tasks/decisions-open-questions.md`. Tick a task only when its acceptance criteria and
verification steps in the plan are met. Run `uv run scripts/check_canon.py` before ticking
anything from Task 2 onward.

## Phase 1 — Foundation
- [x] Task 1: Repository scaffold and `canon/facts.yaml` (S) — deps: none
- [x] Task 2: Consistency checker `scripts/check_canon.py` (S) — deps: T1
- [x] Task 3: Research dossier `lore/research/real-pirate-practices.md` (M) — deps: T1; parallel with T2
- [x] Task 4: Pirate-speak style guide `brand/voice-and-language.md` (S) — deps: T1, T3
- [x] Task 5: Backstory and timeline `lore/backstory.md` (S) — deps: T1, T3

### Checkpoint A — Foundation
- [x] Checker and `--self-test` pass
- [x] Canon, dossier, style guide and backstory are one consistent world
- [x] Human review of the voice before entity work

## Phase 2 — The company
- [x] Task 6: The five bases `lore/bases.md` + `data/bases.csv` (M) — deps: T5
- [x] Task 7: The fleet `lore/fleet.md` + `data/fleet.csv` (M) — deps: T6
- [x] Task 8: Governance, people, articles of agreement (M) — deps: T3, T6
- [x] Task 9: Operations `lore/operations.md` (S) — deps: T7
- [x] Task 10: Brand guidelines `brand/brand-guidelines.md` (S) — deps: T4, T5, T7

### Checkpoint B — The company
- [x] Checker passes; no `TBD` left in canon
- [x] Headcounts, ships and bases reconcile across canon, CSVs and prose
- [ ] Human review: fun, consistent, safe to publish as a demo

## Phase 3 — CSRD knowledge base
- [x] Task 11: Salacia mapping `csrd/salacia-mapping.md` (S) — deps: T6, T7, T8
- [x] Task 12: ESRS 2 general disclosures `csrd/esrs2-general.md` (M) — deps: T8, T9
- [x] Task 13: Double materiality `csrd/double-materiality.md` + `data/iros.csv` (M) — deps: T12
- [x] Task 14: E1 climate `csrd/e1-climate.md` + `data/e1-activity-data.csv` (M) — deps: T7, T13
- [x] Task 15: E2–E5 environment `csrd/e2-e5-environment.md` (S) — deps: T13
- [x] Task 16: S1 own workforce `csrd/s1-workforce.md` + `data/workforce.csv` (M) — deps: T8, T13
- [x] Task 17: S2–S4 value chain, communities, end users (S) — deps: T13
- [x] Task 18: G1 business conduct `csrd/g1-conduct.md` (S) — deps: T9, T13

### Checkpoint C — CSRD knowledge base
- [x] Checker passes
- [x] Every material topic has a topic file; every topic file quotes canon
- [ ] Human review: one topic file read cold, auditor-followable

## Phase 4 — Agent enablement
- [x] Task 19: Root `AGENTS.md` + `CLAUDE.md` (S) — deps: T4, T11
- [x] Task 20: Reporting playbook `agents/reporting-playbook.md` (S) — deps: T12–T19
- [x] Task 21: Worked examples `agents/examples/` (S) — deps: T20
- [ ] Task 22: Dry run with a fresh agent, `tasks/dry-run-1.md` (M) — deps: T21 — SKIPPED on 2026-09-18 at Wybe's request (validation pared back); run later if wanted

### Checkpoint D — Complete
- [x] All acceptance criteria met; checker green
- [ ] Dry-run pass rate ≥ 9/10 recorded
- [ ] Ready for the first Salacia reporting session on behalf of PSI

## Phase 5 — Policies, targets, actions and metrics (planned 2026-11-13)
Milestones FY2026–FY2030 on the Kermis year, plus a 2050 mark; base year FY2024.

### Phase 5a — Framework and pattern
- [x] Task 23: Policy framework: canon `policies:` block, Scope 3 intensity keys, `data/targets.csv` + schema, checker dir, `policies/index.md` (M) — deps: none
- [x] Task 24: E1 climate policy, the pattern-setter (M) — deps: T23

### Checkpoint E — Pattern approved
- [x] Checker passes
- [x] Wybe approves the template and target ambition (2026-11-13: all numbers pre-approved, no approval gate)

### Phase 5b — Environment
- [x] Task 25: E2 pollution policy (S) — deps: Checkpoint E — the 2050 tar-boiled mark must be 10.0 t (canon `e1.scope1_budget_2050_tco2e.tar_and_pitch` = 32.0 at 3.2)
- [x] Task 26: E3 water and marine resources policy (S) — deps: Checkpoint E
- [x] Task 27: E4 biodiversity policy (S) — deps: Checkpoint E
- [x] Task 28: E5 resource use and circularity policy (S) — deps: Checkpoint E
- [x] Task 29: Integrate the environment batch into canon, targets.csv and the topic file (M) — deps: T25–T28 and Wybe's approval of the proposals

### Checkpoint F — Environment complete
- [x] Checker passes; five environment policies live and linked

### Phase 5c — Relations
- [x] Task 30: S1 labour relations policy (S) — deps: Checkpoint E
- [x] Task 31: S2 value-chain workers policy (S) — deps: Checkpoint E
- [x] Task 32: S3 port communities policy (S) — deps: Checkpoint E
- [x] Task 33: S4 consignees and clients policy (S) — deps: Checkpoint E
- [x] Task 34: G1 supplier relations and payment policy; reconcile 96 vs 63 suppliers (S) — deps: Checkpoint E
- [x] Task 35: G1 political engagement policy (S) — deps: Checkpoint E
- [x] Task 36: Integrate the relations batch (M) — deps: T30–T35 and Wybe's approval of the proposals

### Phase 5d — Wiring
- [x] Task 37: Salacia mapping, playbook route, DMA policy coverage (S) — deps: T29, T36

### Checkpoint G — Phase 5 complete
- [x] Checker green
- [x] 11 policies with actions, FY2026–FY2030 trajectory, 2050 mark and metrics
- [ ] Wybe signs off as Quartermaster-General

## Parallel lanes
- After T1: T2 ‖ T3
- After T7: T8 ‖ T9 ‖ T10
- After T13: T14 ‖ T15 ‖ T16 ‖ T17 ‖ T18
- Phase 5: T23 → T24 → Checkpoint E; then T25‖T26‖T27‖T28 → T29 and T30‖T31‖T32‖T33‖T34‖T35 → T36; then T37
