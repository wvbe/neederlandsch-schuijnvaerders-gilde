---
title: Voice an' Language — how the Gilde speaks
status: draft
last-verified: 2026-09-18
canon-refs: [company.short_name, company.abbreviation, company.trade_name_english, scale.fleet_count]
allow-anachronisms: [engine, engines, electricity]  # named only as the things the articles forbid, in the register examples
---

# Voice an' Language — how the Gilde speaks

'Tis the standin' order o' the **Neederlandsch Schuijnvaerders Gilde** (NSG, known in
English ports as *Pirate Shipping Inc*) that every word we set down — be it a bill o'
lading, a letter to a harbourmaster, or a sustainability statement for the regulators in
Brussels — be spoken in the tongue o' the sea. This here guide tells ye how, an' just as
important, tells ye what must **never** be bent, so that the clerks, the auditors an' the
Salacia platform can still read our numbers straight.

Read it afore ye write a line on the Gilde's behalf. Ye be writin' for a company that
means every word; the voice be a house rule, not a costume.

## 1. The boundary: what be never translated

The voice lives in the prose. The **machine layer** stays standard, always, in every
register. If ye break this rule the report cannot be read by the platform, an' the
Quartermaster-General will have words with ye.

| Never translated | Write it as | Example |
| --- | --- | --- |
| Numbers | Digits, thousands separated by commas | 1,944 not "nineteen hundred an' forty-four" |
| Units | SI or the platform's unit name | t CO2e, m³, kg, nautical miles as "nmi" |
| Currency | ISO code before the amount | EUR 480,000,000 or EUR 480 million |
| Dates | ISO 8601 or day-month-year in full | 2025-09-30, or 30 September 2025 |
| Reporting periods | Salacia period key | 102024-092025 |
| ESRS codes an' datapoint names | As the standard writes them | ESRS E1, E1-6, S1-14, GOV-1, IRO-1 |
| Salacia nouns in headers, keys an' tables | Standard English | organization, legal entity, location, reporting year, activity data, emission factor, survey, evidence |
| Legal entity names | Exactly as canon spells them, with English gloss on first use | Crooked Sailors' Guild (Port Royal) Limited |
| Place names an' countries | Real names, ISO 3166 codes in data | Vlissingen, Port Royal, JM |
| People's names an' titles o' office | As canon spells them | Quartermaster-General |
| YAML keys, CSV headers, file names, frontmatter | Plain English, lower case | `shore_headcount` |
| Scope 1, Scope 2, Scope 3 | Untouched | Scope 1 |
| Quoted law an' regulation | Verbatim | Directive (EU) 2022/2464 |

Everything **around** those tokens be pirate speak. A table's header row be machine layer;
its cells may carry a short pirate phrase where a phrase belongs.

## 2. The three registers

One lexicon, three densities. Pick by audience, not by mood.

| Register | Used for | Density | Tells |
| --- | --- | --- | --- |
| **Formal** ("the Council's voice") | Sustainability statement, Salacia narrative datapoints, letters to regulators an' auditors, policies | Light. Every sentence readable by a landsman on first pass. One "aye" per page at most, no "arr" | Complete sentences, "we" or "the Gilde", nautical metaphor kept to one per paragraph, standard term given in brackets at first mention |
| **Internal** ("the logbook voice") | Ship's logs, memos between officers, articles, survey answers meant for the Quartermaster | Medium. Dropped g's, "ye", "me", "th'", oaths mild | Direct address, dates an' watches, short lines, Dutch seasoning (kamer, boekhouder) |
| **Marketing** ("the flag voice") | Client-facing announcements, the brand book, recruitment, the mission | Heavy but clean. Rhythm an' swagger; no cliché from the film reel unless winkin' at it | Imperatives, alliteration, the flag an' the sea in every paragraph |

The same paragraph, three ways:

> **Formal.** In the reportin' year 102024-092025 the Gilde kept a fleet of 25 wooden
> ships under sail. We burned no fuel oil an' bought no electricity <!-- ooc -->(standard
> term, allowed in Scope 2 context)<!-- /ooc -->; our Scope 1 emissions arise from galley
> fires, tar kilns, gunpowder an' lamp oil, an' amount to the figure set out in E1-6 below.
> We do not expect this to change, for our articles forbid an engine aboard any hull we own.

> **Internal.** Log, 30 Sept 2025, end o' the Kermis year. All 25 hulls accounted for.
> Galley wood an' tar be tallied per ship in the boekhouder's ledger; powder spent be in
> the gunner's book. No engine aboard, nor ever will be — the articles say so an' the
> Quartermaster counts the kindlin'. Send the totals to Middelburg by the next galjoot.

> **Marketing.** Twenty-five hulls. Zero engines. Four hundred years o' wind in our sails
> an' not a drop o' oil in our wake. Ye want yer cargo carried the way the sea intended?
> Sign the articles.

## 3. Grammar an' sound

Use these **consistently**; a voice that flickers reads as parody.

**Verbs an' pronouns**
- "be" for *is / are / am* in the present: *the fleet be 25 sail*, *I be the Quartermaster*. Past tense stays regular: *the fleet was*.
- "ye" for *you* (subject an' object). "yer" for *your*. "me" for *my* (*me ledger*). "meself".
- "'tis", "'twas", "'twill" for *it is, it was, it will*.
- "ain't" only in internal an' marketing registers.

**Sounds**
- Drop the final *g* on *-ing* words: *reckonin'*, *sailin'*, *reportin'*. In the formal register, keep it on technical nouns that be part o' the machine layer (*reporting year* stays whole when it be the Salacia term).
- "o'" for *of*, "an'" for *and*, "th'" for *the* (internal an' marketing only; formal writes *the*).
- "afore" (*before*), "'ere" (*here*), "ne'er", "e'er", "o'er", "'em" (*them*), "'bout".
- "aye" an' "nay". "Arr" be permitted in marketing an' internal only, once per document, an' never as a sentence on its own.

**Address an' titles**
- Officers by office: *Cap'n*, *Quartermaster*, *the Boekhouder*, *the Lords Five*, *the Council*.
- Crews collectively: *the hands*, *the company*, *all hands*, *me hearties* (internal an' marketing only).
- Outsiders: *landsmen*, *the regulators*, *the good folk o' Brussels*, *the auditor* (never mocked).

**Dutch seasoning.** The Gilde be Zeeuws. Use these as proper nouns, not translated:
*kamer* (chamber), *boekhouder* (bookkeeper), *retourschip*, *fluyt*, *jacht*, *galjoot*,
*gulden* an' *stuiver*, *Heeren Vijf*, *Raad van Kapiteins*, *commissie* (a letter o'
marque), *prijs* (a prize). One per paragraph be plenty.

**Oaths.** Mild an' maritime only: *blow me down*, *by the Lords Five*, *sink me*, *strike
me colours*. No profanity, no religious slurs, nothin' aimed at a real people or nation.

## 4. Nautical metaphor bank

Reach for the sea when a landsman would reach for a boardroom. One per paragraph in the
formal register; freer elsewhere.

| Landsman says | The Gilde says |
| --- | --- |
| strategy | our course, the course we've set |
| risk | weather, shoals, lee shore |
| opportunity | fair wind, a following sea |
| target | the mark we steer for |
| governance | the articles, the watch bill, who holds the helm |
| stakeholder | shipmate, harbourmaster, all who sail with us or trade with us |
| supply chain | the chandlers, rope-walks an' yards that fit us out |
| annual report | the reckonin' o' the year |
| audit | the muster, the Quartermaster's count |
| policy | standin' order |
| incident | a squall, a fouled anchor, a man overboard |
| headcount | souls aboard, hands |
| profit | the share, the prize money |
| loss | a hull lost, a lean year |
| compliance | sailin' within the commissie |

## 5. The CSRD glossary

Formal register rule: **first mention gives the Gilde's term an' the standard term in
brackets; thereafter either may be used.** Datapoint and requirement codes stay standard
always.

| Standard term | The Gilde's term |
| --- | --- |
| Corporate Sustainability Reporting Directive (CSRD) | the Brussels Articles |
| European Sustainability Reporting Standards (ESRS) | the Standards (never translated in code form) |
| sustainability statement | the reckonin' o' the year |
| double materiality assessment (DMA) | the reckonin' o' what matters |
| impact materiality | what we do to the world |
| financial materiality | what the world does to our purse |
| impacts, risks and opportunities (IROs) | our wake, our weather an' our fair winds |
| material topic | a matter that weighs |
| value chain | all who fit us out an' all who take our cargo |
| upstream | windward o' us |
| downstream | leeward o' us |
| own operations | aboard an' ashore |
| own workforce (S1) | our hands |
| workers in the value chain (S2) | the hands that fit us out |
| affected communities (S3) | the folk o' the ports |
| consumers and end-users (S4) | them as take delivery |
| business conduct (G1) | conduct under the articles |
| climate change (E1) | the warmin' o' the seas |
| greenhouse gas emissions | smoke |
| Scope 1 | Scope 1 (our own smoke) |
| Scope 2 | Scope 2 (smoke bought in; we buy none) |
| Scope 3 | Scope 3 (smoke o' them as fit us out) |
| emission factor | the smoke per measure |
| activity data | the tally (o' wood, tar, powder, oil) |
| energy consumption | what we burn an' what the wind gives free |
| transition plan | the course to a cleaner wake |
| target | the mark |
| base year | the year we measure from |
| pollution (E2) | what fouls the water an' the air |
| water and marine resources (E3) | fresh water an' the sea's bounty |
| biodiversity and ecosystems (E4) | the livin' coasts an' forests |
| resource use and circular economy (E5) | makin' do an' makin' over |
| policy | standin' order |
| action | what we've done about it |
| metric | the measure |
| governance body | the Council an' the Lords Five |
| administrative, management and supervisory bodies | the Raad van Kapiteins (management) an' De Heeren Vijf (supervisory) |
| due diligence | lookin' afore we board |
| remediation | makin' it right |
| grievance mechanism | the parley |
| whistleblower | the hand who calls the Quartermaster |
| collective bargaining | the vote o' all hands under the articles |
| health and safety | life an' limb |
| work-related injury | a hurt taken in the Gilde's service |
| training | learnin' the ropes |
| living wage | a share a hand can live on |
| forced labour | pressin' (abolished) |
| child labour | boys aboard (none; all hands be grown) |
| anti-corruption | no gifts to harbourmasters beyond the articles |
| legal entity | kamer (chamber) — but the entity name itself stays standard |
| location | a base or a hull |
| reporting year | the Kermis year (the period key stays standard) |
| organization | the Gilde |
| evidence file | the papers (ledger page, logbook leaf, notary's count) |
| survey | the muster o' questions |
| Salacia platform | the Salacia platform (never renamed) |

## 6. Do an' don't

**Do**
- Keep every number, unit, code an' name exactly as canon an' the standard write them.
- Give the standard term in brackets at first mention in the formal register.
- Write complete sentences in the formal register; an auditor must follow on first read.
- Prefer a period word from the research dossier to a film word: *commissie* over "pirate licence", *careenin'* over "dry dock".
- Let the humour come from the collision o' 1600s means an' 2020s duties, never from mockin' the duty.
- Say plainly when a fact be missing: mark it `[UNCHARTED]` an' propose it to canon.

**Don't**
- Don't translate anythin' in the boundary table.
- Don't write "arr" in the formal register, or more than once anywhere.
- Don't invent a ship, a base, a person or a number that canon does not hold.
- Don't reach for the film reel: no "shiver me timbers", no "walk the plank", no "X marks the spot", no parrots — except as a knowin' wink in marketing, once.
- Don't imitate any real accent or people. The voice be a house voice, not an impression.
- Don't let the voice bury a bad number. If a hand was hurt, the sentence says so first.

## 7. On authenticity an' caricature

The "pirate accent" as landsmen know it comes not from the 1600s but from a West Country
actor in a picture o' 1950. We know this, an' we use the voice anyway, as a house style,
with our eyes open. What keeps it honest be the record: the research dossier in
`../lore/research/real-pirate-practices.md` holds what real crews did, how they governed
themselves, what they were paid an' what they were owed when hurt. Prefer its words.

Our crews were, an' be, gathered from every coast we touch. The voice belongs to the
Gilde, not to any nation or people; no character be written with a mock accent o' a real
ethnic group, an' no joke rests on one.

## 8. Formatting rules for documents

- Headings may be in pirate speak. Table header rows be machine layer (standard English).
- Frontmatter, YAML keys, CSV headers an' file names be plain English, lower case, hyphen or underscore.
- Thousands take commas; decimals take a point; percent be written "%".
- A Salacia narrative datapoint be one to four paragraphs o' formal register, no headings inside it.
- A quantitative datapoint be the number, the unit, the period key an' one sentence o' formal register naming the source file.
- Where a word from `../canon/anachronisms.txt` must be quoted because the standard demands it, allow it in the file's frontmatter (`allow-anachronisms:`) with a reason in a comment, or set it inside an out-of-character block. Never use such a word as the Gilde's own gear.

## Related

- [Brand guidelines](brand-guidelines.md) — flag, colours, type, naming
- [Research dossier](../lore/research/real-pirate-practices.md) — the record the voice leans on
- [Canon](../canon/facts.yaml) — the numbers an' names
- [Decisions](../tasks/decisions-open-questions.md) — why the Gilde be shaped as it be
