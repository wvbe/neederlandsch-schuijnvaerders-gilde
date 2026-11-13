---
title: Brand Guidelines o' the Neederlandsch Schuijnvaerders Gilde
status: draft
last-verified: 2026-11-13
canon-refs: [company.legal_name, company.abbreviation, company.trade_name_english, company.english_gloss, company.motto, company.motto_gloss, scale.fleet_count, scale.base_count, company.founded_year]
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

**Motto.** **VENTO SOLO** (by wind alone). Latin, in capitals, with a raised point between
the words where the letterin' allows: VENTO · SOLO. It rides the ribbon o' the coat o' arms.
Never translate it in display; give the gloss once, in brackets, an' then leave it be, as
with our name.

**Mission.** *To carry what others dare not, by wind alone, under articles every hand has
signed.* The motto be the mission cut down to two words.

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
- **Charge:** a lead-white fluyt heelin' on a runnin' sea, set over the bend, sails full.
- **Hoist:** five minium-orange rings in a column, one for each chamber; the top ring be
  Vlissingen.

The drawin' to follow be the [shield](shield.png), the heart o' the
[coat o' arms](coat-of-arms.png) drawn on its own; where these words an' the arms disagree,
the arms win. On a black ground the rings may be omitted for
very small marks (a wax seal, a hull number), never the ship.

## 4. The coat o' arms

The coat o' arms be the Gilde's ceremonial mark: the front page o' this knowledge base, the
cover o' the reckonin' o' the year an' the brand book. The flag stays the everyday mark on
hull, door an' document. The drawin' be [`coat-of-arms.png`](coat-of-arms.png).

- **Shield:** the flag itself: a dark field, the bend risin' from the lower hoist to the
  upper fly, the fluyt heelin' over it on a runnin' sea, an' the five rings down the hoist.
- **Crest:** a crown upon the shield; above it the NSG monogram on a merchant's staff an'
  cross-bar, set between ANNO an' 1621.
- **Supporters:** two lions rampant, crowned, holdin' the shield.
- **Mantlin':** acanthus leaves, engraved.
- **Motto:** VENTO · SOLO on a ribbon beneath the shield.
- **Name:** the Gilde's name on a tablet below the ribbon, an' *Vlissingen* beneath it.

Reproduce the arms whole, from the master file; never redraw a part of it. Below 30 mm or
120 px use the [shield](shield.png) alone, from its own master file, never the arms shrunk.

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
