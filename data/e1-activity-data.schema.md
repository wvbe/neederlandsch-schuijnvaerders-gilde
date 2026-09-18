# E1 activity data — schema

One row per legal entity, location, period and activity: the tally of wood, charcoal, tar,
powder, oil, tallow, livestock and purchased goods that the Salacia platform matches to an
emission factor to produce the ESRS E1 inventory. Locations are the 25 hulls of
`fleet.csv` and the 5 chambers of `bases.csv`, exactly as those registers spell them.
Both reported years are present: `102024-092025` (FY2025) and `102023-092024` (FY2024).
Scope 2 has no rows, because the Gilde buys no electricity, heat or steam; the reasoning
is in `../csrd/e1-climate.md` under E1-6. Prose, emission factors, calorific values and
the totals computed from these rows live in that file. Fields containing commas are quoted.

| Column | Description |
| --- | --- |
| period_key | Salacia period key of the reporting year: `102024-092025` or `102023-092024` |
| legal_entity | Exact legal entity name of the chamber the location belongs to, as `bases.csv` spells it |
| location | Hull name from `fleet.csv` for a hull, or `chamber_name` from `bases.csv` for a base |
| location_kind | `hull` or `base` |
| activity_category | Grouping of the activity: galley fuel, yard fuel, gunpowder, lighting, livestock, purchased goods, capital goods, business travel, end-of-life |
| activity | Plain-English name of what was burned, carried, bought, built or broken up |
| quantity | Amount consumed or purchased in the period, as a number |
| unit | Unit the platform's unit standardisation resolves: kg, tonne, litre, head, pkm, unit |
| scope | GHG Protocol scope of the row: `1` or `3` (no `2` rows exist) |
| emission_factor_hint | Emission-factor category to match; Scope 3 rows also carry the category number, for example `Scope 3 cat 1 purchased goods: sawn oak` |
| source_document | Evidence the row rests on, named as in `../csrd/salacia-mapping.md` section 6: ledger page, gunner's book or careenin' record |
| note | Optional remark from the ledger or the careenin' record; may be empty |

```columns
period_key
legal_entity
location
location_kind
activity_category
activity
quantity
unit
scope
emission_factor_hint
source_document
note
```
