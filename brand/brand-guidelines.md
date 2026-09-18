---
title: Brand Guidelines o' the Neederlandsch Schuijnvaerders Gilde
status: draft
last-verified: 2026-09-18
canon-refs: [company.legal_name, company.abbreviation, company.trade_name_english, company.english_gloss, scale.fleet_count, scale.base_count, company.founded_year]
allow-anachronisms: [engines]  # named once, as the thing the Gilde lacks, in the on-brand example
---

# Brand Guidelines o' the Neederlandsch Schuijnvaerders Gilde

## 1. Who we be

**Neederlandsch Schuijnvaerders Gilde N.V.** — the Netherlandish Guild of Crooked Sailors —
short **NSG**, an' in every English-speakin' port simply **Pirate Shipping Inc**. Founded
at Vlissingen anno 1621, we be a fleet of 25 wooden ships an' 5 chambers of operation,
carryin' the cargo no landsman's line will touch: spices, valuables an' exotic materials,
between the Low Countries, the British an' Irish coasts, the Caribbean, the Indian Ocean,
the spice islands an' the wide Pacific. An' when a client holds a commissie against a
rival's freight, we be the ones who serve it.

**Mission.** *To carry what others dare not, by wind alone, under articles every hand has
signed.*

**Promise to the client.** Yer cargo arrives, or the Gilde pays the share. Yer commissie
be served within the articles, or not at all.

**What we be not.** We be not a museum, not a theme park an' not a joke. The sails be the
means; the trade be real; the reckonin' be honest.

## 2. The name

| Form | Use |
| --- | --- |
| Neederlandsch Schuijnvaerders Gilde N.V. | Legal documents, the sustainability statement's cover, contracts |
| Neederlandsch Schuijnvaerders Gilde | First mention in any document |
| the Gilde | Every mention thereafter |
| NSG | Tables, data, hull marks, ledgers |
| Pirate Shipping Inc | English-language trade, client-facin' marketing, harbour registers where the Dutch name will not fit the form |

Spell it as the founders did: *Neederlandsch*, *Schuijnvaerders*, *Gilde*. Never modernise
the spellin'; never put an apostrophe in *Schuijnvaerders*. The English gloss ("Guild of
Crooked Sailors") be given once, in brackets, an' then left alone.

## 3. The flag

The flag be the mark on every hull, every warehouse door an' every document's cover.

- **Field:** tar black, the whole cloth.
- **Bend:** a band o' indigo from the lower hoist to the upper fly — the *schuijn*, the
  slant that names us.
- **Charge:** a lead-white fluyt heelin' hard to leeward, set over the bend, sails full.
- **Hoist:** five minium-orange rings in a column, one for each chamber; the top ring be
  Vlissingen.

The drawin' be in [`assets/flag.svg`](assets/flag.svg). Reproduce it in these four colours
only. On a black ground the rings may be omitted for very small marks (a wax seal, a hull
number), never the ship.

## 4. Colours

Named for the pigments a 1650 sailmaker or painter would have mixed, given with modern
values for landsmen's screens an' presses.

| Name | Pigment | Value | Use |
| --- | --- | --- | --- |
| Tar Black | lamp black bound in tar | #1B1A17 | Flag field, body text, hull marks |
| Indigo Bend | indigo (imported from the Indies we sail to) | #2E3A5F | The bend, headings, rules |
| Lead White | lead white (loodwit) | #E9E4D6 | Paper an' sailcloth grounds, the ship on the flag |
| Minium Orange | red lead (menie) | #C8501E | The five rings, warnings, the seal |
| Verdigris | copper green | #5C8A6B | Tables o' the environment topics, "on course" marks |
| Ochre | yellow ochre | #B9975B | Ledger rules, secondary text, the guilder column |
| Vermilion | cinnabar | #9E2A2B | Injuries an' incidents; never decorative |

Never use a blue brighter than Indigo Bend: the bright Prussian blue o' later centuries
did not exist in our founders' day an' looks wrong on our cloth.

## 5. Type

Our founders' punchcutters were Dutch, an' the types cut by Van Dijck an' Voskens in the
1670s still exist as the Fell types. Use them.

| Role | Face | Fallback |
| --- | --- | --- |
| Display an' document titles | IM Fell Double Pica | IM Fell English, then Georgia |
| Body text | IM Fell English | EB Garamond, then Georgia |
| Machine layer (tables, data, codes, period keys) | a plain monospaced face for codes; the body face for tables | Courier for codes |

Set body text generously leaded; the Fell faces be dark. Never use a sans-serif for the
Gilde's own words. Ligatures on; old-style figures in prose, linin' figures in tables.

## 6. Namin' conventions

**Hulls.** Every ship carries a hull mark `NSG-01` to `NSG-25` in the register an' a name
in the language o' her chamber of enrolment, in that language's old spellin' where one
exists. By type:

| Type | Named for | Example shape |
| --- | --- | --- |
| retourschip | Zeeland an' Holland towns an' waters, old spellin' | *Zierickzee*, *Ter Veere* |
| jacht | birds o' the sea an' o' prey | *De Stormvoghel*, *The Gannet* |
| fluyt | virtues, in old Dutch, chosen with a straight face | *Gheduld*, *Voorsichticheyt* |
| interdiction sloop | weather an' sea states | *Windvlaeg*, *Squall*, *La Rafale* |
| galjoot | messengers an' haste | *De Bode*, *Postillon* |

Names be given by the chamber an' entered in `../data/fleet.csv`; no hull be renamed
without a vote o' her company.

**Chambers.** *Kamer Vlissingen*, *Chamber of Baltimore*, *Chamber of Port Royal*,
*Chambre de Sainte-Marie*, *Kamar Ambon*. The legal entity name stays as canon spells it.

**Documents.** `<chamber code>-<Kermis year>-<serial>`: `VL-2025-014`. Chamber codes: VL,
BA, PR, SM, AM. The Kermis year be named for the calendar year in which it ends.

**People.** Office afore name: *Quartermaster-General Such-and-such*. Crew be "hands", never
"staff" or "employees" outside the machine layer.

## 7. Tone by audience

| Audience | Register | The line we hold |
| --- | --- | --- |
| Regulators, auditors, the Salacia platform | Formal | Every number straight, every claim traceable to a ledger; humour only in the collision o' old means an' new duties |
| Clients | Marketing for the pitch, formal for the contract | Confidence without boast; the articles quoted, never waved |
| Our hands | Internal | Plain, direct, respectful; bad news first |
| Port authorities an' harbourmasters | Formal, brief | Courteous; no gifts beyond the articles, an' say so |
| The press an' the curious | Marketing | The flag voice, one wink at the film reel at most |

## 8. On brand, off brand

**On brand**
> "Twenty-five hulls, five chambers, no engines. Ye'll have yer nutmeg in Vlissingen by the Kermis, or the Gilde pays the share."

> "In the year 102024-092025 the Gilde suffered 41 hurts taken in its service, set out in S1-14 below. Each was paid under the articles' schedule within the month. We say this first, afore any fair wind." <!-- ooc -->(illustrative number; the real figure lives in canon once Task 16 sets it)<!-- /ooc -->

**Off brand**
> "Arrr! Shiver me timbers, matey, our synergies be leveragin' a best-in-class logistics solution!" — three film words, one landsman's phrase, no fact.

> "NSG is a modern maritime logistics provider committed to sustainable operations." — true in substance, dead in voice.

## Related

- [Voice an' language](voice-and-language.md) — the registers, the lexicon, the boundary
- [Fleet register](../data/fleet.csv) — hull marks an' names
- [Canon](../canon/facts.yaml) — the names an' numbers this book quotes
