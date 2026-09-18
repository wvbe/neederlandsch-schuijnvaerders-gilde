# Fleet register — schema

One row per hull, 25 in all, NSG-01 to NSG-25. Crew per type is fixed by canon
`fleet_mix` (220, 90, 18, 70, 15) so that the `crew` column sums to canon
`scale.seagoing_headcount`. Prose about the ships lives in `../lore/fleet.md`. Fields
containing commas are quoted.

| Column | Description |
| --- | --- |
| hull_id | Hull mark in the register, `NSG-01` to `NSG-25`; the key of the row |
| name | Ship's name in the language of her chamber, old spelling where one exists (brand guidelines section 6) |
| type | Canon ship type: retourschip, jacht, fluyt, sloep or galjoot |
| type_english | English name of the type as canon `fleet_mix` gives it |
| chamber_key | Canon base key of the chamber of enrolment; matches `key` in `bases.csv` |
| chamber_code | Two-letter chamber code (VL, BA, PR, SM, AM); matches `chamber_code` in `bases.csv` |
| launch_year | Year the present wooden hull was launched (1960 to 2024); the name may be older |
| tons | Burden of the hull in tons, approximate |
| crew | Seagoing hands aboard; fixed per type by canon `fleet_mix.crew_each` |
| guns | Number of muzzle-loading cannon carried |
| role | Operational role: cargo, mixed, interdiction or dispatches |
| typical_route | Usual voyage or cruising ground, place names as commonly written |
| crew_parten_share | Fraction of the hull held collectively by her company as a minority "parten" interest |
| note | One-line character note in the internal register |

```columns
hull_id
name
type
type_english
chamber_key
chamber_code
launch_year
tons
crew
guns
role
typical_route
crew_parten_share
note
```
