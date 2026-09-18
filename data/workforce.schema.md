# Workforce register — schema

One row per reporting year, legal entity, location, role group, contract type, gender and
country-of-origin region: the muster roll of the Gilde's own workforce, aggregated to
headcounts so that no row identifies a hand. Locations are the 25 hulls of `fleet.csv` and
the 5 chambers of `bases.csv`, spelled exactly as those registers spell them. Both reported
years are present: `102024-092025` (FY2025) and `102023-092024` (FY2024). For FY2025 the
rows sum per hull to that hull's `crew` in `fleet.csv` and per base to that chamber's
`shore_headcount` in `bases.csv`; FY2024 differs by the hands who had not yet been enrolled
or had left. Prose, rates, targets and the health-and-safety metrics computed from these
rows live in `../csrd/s1-workforce.md`. Fields containing commas are quoted.

| Column | Description |
| --- | --- |
| period_key | Salacia period key of the reporting year: `102024-092025` or `102023-092024` |
| legal_entity | Exact legal entity name of the chamber the location belongs to, as `bases.csv` spells it |
| location | Hull name from `fleet.csv` for a hull, or `chamber_name` from `bases.csv` for a base |
| location_kind | `hull` or `base` |
| role_group | Rating group of the hands counted: officer, able hand, ordinary hand, surgeon or carpenter or sailmaker, gunner, shore clerk, yard hand, warehouse hand, victualler |
| contract_type | `articled on shares` for a hand paid on the share ladder, `waged ashore` for a hand paid a wage at a chamber |
| gender | Gender as the hand states it at the muster: `woman`, `man`, or `other or not stated` |
| country_of_origin_region | Region the hand gives as country of origin: Netherlands, Ireland, United Kingdom, Caribbean, East Africa and Madagascar, South and South East Asia, Pacific islands, other |
| headcount | Number of hands in the cell, as a whole number; every row is 1 or more |

```columns
period_key
legal_entity
location
location_kind
role_group
contract_type
gender
country_of_origin_region
headcount
```
