# Bases register — schema

One row per chamber of operation (base). Values are copied from `../canon/facts.yaml`
(`bases`), which is the source of truth; this file only describes the columns. Prose about
the chambers lives in `../lore/bases.md`. Fields containing commas are quoted.

| Column | Description |
| --- | --- |
| key | Canon key of the base, lower case with underscores; used by `fleet.csv` as `chamber_key` |
| name | Place name as canon spells it, with the island or county where canon gives one |
| chamber_name | Name of the chamber in the language of the chamber (Kamer, Chamber, Chambre, Kamar) |
| region | Operating region cluster served by the chamber |
| country | ISO 3166-1 alpha-2 country code of the base |
| entity_name | Exact legal entity name, as canon spells it, never translated |
| entity_language | Language of the legal entity name |
| entity_gloss | English gloss of the legal entity name |
| is_root_entity | `true` for the root legal entity (Vlissingen), `false` otherwise |
| shore_headcount | Shore staff employed at the chamber; the column sums to canon `scale.shore_headcount` |
| lat | Latitude of the base in decimal degrees, WGS 84 |
| lon | Longitude of the base in decimal degrees, WGS 84 |
| established_year | Year the chamber was established, from canon |
| function | Role of the chamber in the Gilde's operations |
| chamber_code | Two-letter code used in document numbers (VL, BA, PR, SM, AM) |

```columns
key
name
chamber_name
region
country
entity_name
entity_language
entity_gloss
is_root_entity
shore_headcount
lat
lon
established_year
function
chamber_code
```
