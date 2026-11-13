# Target register — schema

One row per mark (target) set in a written policy under `../policies/`. This file is the
machine layer of the target tables in those policies and the one place the year-by-year
milestones are held. The headline 2030 and 2050 marks are also held in canon, beside the
metric's FY2025 value; where a row names a canon key, the cell must equal canon, and canon
wins if they disagree.

Years are Kermis years (1 October to 30 September). The base year is FY2024 (`102023-092024`)
and the reported year FY2025 (`102024-092025`). The `fy2026` to `fy2030` cells are
**milestones**, the mark for that year, not outcomes. An outcome for FY2026 or later is not
held here. A cell is empty where no value exists, for example a metric first counted in
FY2025. Booleans are `true` or `false`. Fields containing commas are quoted.

| Column | Description |
| --- | --- |
| target_id | Identifier of the row, `<policy suffix>-T<n>`, for example `E1-T1`; stable across years |
| policy_id | The policy the mark belongs to, as canon `policies[].id` spells it, for example `POL-E1` |
| topic_code | ESRS topic code: `E1` to `E5`, `S1` to `S4`, `G1` |
| esrs_dr | Disclosure requirement the target answers, for example `E1-4` |
| metric | One line naming the measure, in plain English |
| unit | The unit as the platform would write it: `tCO2e`, `t`, `m3`, `%`, `count`, `days`, `EUR`, `ha`, `boolean`, or a compound such as `tCO2e per million tonne-nmi` |
| kind | `absolute` or `relative` (intensity or share), as ESRS 2 MDR-T asks |
| direction | `decrease`, `increase` or `hold` (keep at the stated level every year) |
| scope | Where the mark applies: `all chambers and hulls`, a named chamber key, a hull class, or `value chain` |
| base_fy2024 | Value in the base year FY2024 |
| fy2025 | Value in the reported year FY2025 |
| fy2026 | Milestone for FY2026 |
| fy2027 | Milestone for FY2027 |
| fy2028 | Milestone for FY2028 |
| fy2029 | Milestone for FY2029 |
| fy2030 | Milestone for FY2030; equals the canon 2030 mark where `canon_key_2030` is filled |
| fy2050 | The long mark for FY2050; equals canon where `canon_key_2050` is filled |
| canon_key_2030 | Canon key of the 2030 mark, for example `e1.target_2030_scope1_tco2e`; empty if canon holds none |
| canon_key_2050 | Canon key of the 2050 mark; empty if canon holds none |
| source_file | Policy file under `../policies/` where the mark is stated and explained |

```columns
target_id
policy_id
topic_code
esrs_dr
metric
unit
kind
direction
scope
base_fy2024
fy2025
fy2026
fy2027
fy2028
fy2029
fy2030
fy2050
canon_key_2030
canon_key_2050
source_file
```
