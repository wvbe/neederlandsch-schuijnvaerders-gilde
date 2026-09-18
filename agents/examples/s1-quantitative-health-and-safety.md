---
title: "Example — S1-14 quantitative datapoints with commentary (formal register)"
status: draft
last-verified: 2026-09-18
register: formal
request: "Salacia quantitative datapoints for ESRS S1-14 health and safety metrics, periods 102024-092025 and 102023-092024, with a short commentary"
sources: [csrd/s1-workforce.md §S1-14, data/workforce.csv, canon s1.*]
canon-refs: [s1.hurts_fy2025, s1.hurts_fy2024, s1.fatalities_fy2025, s1.hurts_per_million_hours_fy2025, s1.hurts_per_million_hours_fy2024, s1.hours_worked_fy2025, s1.hours_worked_fy2024, s1.matanzas_payments_count_fy2025, s1.matanzas_payments_eur_fy2025, s1.matanzas_payments_eur_fy2024, s1.hurts_falls_from_aloft_fy2025, s1.hurts_scurvy_fy2025]
---

# Example — S1-14, life an' limb

**Request.** Fill the S1-14 quantitative datapoints for both periods an' add a commentary
the auditor can read.

**Answer as submitted**

| Datapoint | Unit | 102023-092024 | 102024-092025 | Source |
| --- | --- | --- | --- | --- |
| Fatalities as a result of work-related injuries | headcount | 0 | 0 | surgeon's reports; canon s1.fatalities_fy2024, s1.fatalities_fy2025 |
| Recordable work-related accidents | count | 54 | 47 | surgeon's reports; canon s1.hurts_fy2024, s1.hurts_fy2025 |
| Rate of recordable work-related accidents | per 1,000,000 hours worked | 9.5 | 8.2 | derived; canon s1.hurts_per_million_hours_fy2024, s1.hurts_per_million_hours_fy2025 |
| Hours worked (derived from the watch bill) | hours | 5,656,200 | 5,712,400 | canon s1.hours_worked_fy2024, s1.hours_worked_fy2025 |
| Matanzas schedule payments made | count | 11 | 9 | Matanzas ledger; canon s1.matanzas_payments_count_fy2024, s1.matanzas_payments_count_fy2025 |
| Matanzas schedule payments made | EUR | 151,000 | 106,000 | Matanzas ledger; canon s1.matanzas_payments_eur_fy2024, s1.matanzas_payments_eur_fy2025 |

```text
Commentary (formal register). Forty-seven hands took a hurt in the Gilde's service
(recordable work-related accidents) in 102024-092025, against 54 the year afore; none
died, in either year. The rate be 8.2 per 1,000,000 hours worked, down from 9.5, on hours
we derive from the watch bill rather than measure, for the Gilde keeps no clock but the
sandglass an' says so. Falls from aloft remain the commonest hurt at 14, an' 9 hands took
scurvy on the long southern passages, which be nine too many for a company that has known
the cure since afore it had a name; the victuallin' order on citrus be tightened in
consequence. Nine hurts met the Matanzas schedule (the Gilde's social protection scheme)
an' EUR 106,000 was paid from the common chest within the month, as the articles require.
Every hurt be in the surgeon's report o' the hull or hard where it was taken, an' every
payment in the Matanzas ledger kept by the Quartermaster-General.

Sources: canon: s1.hurts_fy2025, s1.hurts_fy2024, s1.fatalities_fy2025,
s1.hurts_per_million_hours_fy2025, s1.hours_worked_fy2025, s1.matanzas_payments_eur_fy2025;
csrd/s1-workforce.md §S1-14; data/workforce.csv
```

**Why it passes.** Numbers, units an' period keys in the machine layer exactly as canon
holds them; the derivation o' hours declared; the worst figures (the falls, the scurvy)
said in the commentary rather than left in the table; a canon key for every cell.
