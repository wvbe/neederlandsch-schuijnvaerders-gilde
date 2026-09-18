---
title: The Salacia Mappin' — how the Gilde be set up on the platform
status: draft
last-verified: 2026-09-18
canon-refs: [company.legal_name, reporting.fiscal_year_start_month, reporting.reported_year_key, reporting.base_year_key, scale.fleet_count, scale.base_count, scale.seagoing_headcount, scale.shore_headcount, scale.total_headcount]
allow-anachronisms: [upload, spreadsheet]  # the platform's own words for the landsman's act, quoted once each in section 7
---

# The Salacia Mappin' — how the Gilde be set up on the platform

This file tells an agent, in one place, how the Gilde's world maps onto the platform's
nouns: organization, reporting year, legal entity, location, product, role an' evidence.
The platform's words stay the platform's words (see the boundary table in
[voice an' language](../brand/voice-and-language.md)); everythin' else be ours.

## 1. Organization

| Platform field | Value |
| --- | --- |
| Organization name | Neederlandsch Schuijnvaerders Gilde N.V. |
| Trade name shown to English-speakin' clients | Pirate Shipping Inc |
| Reporting-year start month | 10 |
| Reporting year (this reckonin') | 102024-092025 |
| Base year | 102023-092024 |
| Currency | EUR |
| Standards reported | ESRS (under CSRD), voluntary early adoption; VSME composition available from the same data |
| Enabled products | csrd-report, dma, surveys, custom-surveys, E1 activity data an' calculation, E2 to E5, S1 to S4, G1, ESRS 2 narrative datapoints, reduction plan |

The Gilde's year runs from 1 October to 30 September an' be called the Kermis year; the
platform derives the period key from the start month, so `102024-092025` be FY2025 an'
`102023-092024` be FY2024. Both years be declared; FY2024 be the year we measure from.

## 2. Legal entities, declared for the reportin' year

One root an' five chambers. The Vlissingen chamber **be** the root entity; the other four
be subsidiaries declared under it for `102024-092025`. Entity names stay exactly as
written here in every datapoint.

| Legal entity | English gloss | Chamber | Country | Role in the year | Shore hands |
| --- | --- | --- | --- | --- | --- |
| Neederlandsch Schuijnvaerders Gilde N.V. | Netherlandish Guild of Crooked Sailors, public company | Kamer Vlissingen | NL | root | 120 |
| Crooked Sailors' Guild of Baltimore Limited | Crooked Sailors' Guild of Baltimore | Chamber of Baltimore | IE | subsidiary | 45 |
| Crooked Sailors' Guild (Port Royal) Limited | Crooked Sailors' Guild, Port Royal | Chamber of Port Royal | JM | subsidiary | 70 |
| Guilde des Navigateurs Obliques de Sainte-Marie SARL | Guild of Oblique Navigators of Sainte-Marie | Chambre de Sainte-Marie | MG | subsidiary | 50 |
| PT Gilda Pelayar Serong Ambon | Guild of Crooked Sailors of Ambon, limited company | Kamar Ambon | ID | subsidiary | 65 |

The same six entities be declared for the base year `102023-092024`; no chamber was opened,
closed or merged between the two years.

## 3. Locations

Every chamber be a location under its own entity, an' **every hull be a location under the
entity o' the chamber where she be enrolled**. That gives 5 base locations an' 25 hull
locations, so activity data (wood, tar, powder, oil) an' hands can be tallied per hull an'
rolled up per chamber. A hull's location does not move when she sails; her smoke be booked
to her chamber wherever she burns it.

### Bases

| Location | Kind | Legal entity | Place | Hands |
| --- | --- | --- | --- | --- |
| Kamer Vlissingen | base | Neederlandsch Schuijnvaerders Gilde N.V. | Vlissingen | 120 |
| Chamber of Baltimore | base | Crooked Sailors' Guild of Baltimore Limited | Baltimore, West Cork | 45 |
| Chamber of Port Royal | base | Crooked Sailors' Guild (Port Royal) Limited | Port Royal, Jamaica | 70 |
| Chambre de Sainte-Marie | base | Guilde des Navigateurs Obliques de Sainte-Marie SARL | Île Sainte-Marie (Nosy Boraha), Madagascar | 50 |
| Kamar Ambon | base | PT Gilda Pelayar Serong Ambon | Ambon, Moluccas | 65 |

### Hulls

| Location | Kind | Legal entity | Enrolment | Crew |
| --- | --- | --- | --- | --- |
| Zierickzee (NSG-01) | hull, retourschip | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 220 |
| Ter Veere (NSG-02) | hull, retourschip | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 220 |
| Middelburgh (NSG-03) | hull, retourschip | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 220 |
| De Honte (NSG-04) | hull, retourschip | PT Gilda Pelayar Serong Ambon | enrolled at Kamar Ambon | 220 |
| De Stormvoghel (NSG-05) | hull, jacht | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 90 |
| The Gannet (NSG-06) | hull, jacht | Crooked Sailors' Guild of Baltimore Limited | enrolled at Chamber of Baltimore | 90 |
| The Frigate Bird (NSG-07) | hull, jacht | Crooked Sailors' Guild (Port Royal) Limited | enrolled at Chamber of Port Royal | 90 |
| The Pelican (NSG-08) | hull, jacht | Crooked Sailors' Guild (Port Royal) Limited | enrolled at Chamber of Port Royal | 90 |
| Le Paille-en-queue (NSG-09) | hull, jacht | Guilde des Navigateurs Obliques de Sainte-Marie SARL | enrolled at Chambre de Sainte-Marie | 90 |
| Elang Laut (NSG-10) | hull, jacht | PT Gilda Pelayar Serong Ambon | enrolled at Kamar Ambon | 90 |
| Gheduld (NSG-11) | hull, fluyt | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 18 |
| Voorsichticheyt (NSG-12) | hull, fluyt | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 18 |
| Trouwe (NSG-13) | hull, fluyt | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 18 |
| Rechtvaerdicheyt (NSG-14) | hull, fluyt | Crooked Sailors' Guild of Baltimore Limited | enrolled at Chamber of Baltimore | 18 |
| Eendraght (NSG-15) | hull, fluyt | Crooked Sailors' Guild (Port Royal) Limited | enrolled at Chamber of Port Royal | 18 |
| Matigheyt (NSG-16) | hull, fluyt | Guilde des Navigateurs Obliques de Sainte-Marie SARL | enrolled at Chambre de Sainte-Marie | 18 |
| Neersticheyt (NSG-17) | hull, fluyt | PT Gilda Pelayar Serong Ambon | enrolled at Kamar Ambon | 18 |
| Spaersaemheyt (NSG-18) | hull, fluyt | PT Gilda Pelayar Serong Ambon | enrolled at Kamar Ambon | 18 |
| The Sou'wester (NSG-19) | hull, sloep | Crooked Sailors' Guild of Baltimore Limited | enrolled at Chamber of Baltimore | 70 |
| Squall (NSG-20) | hull, sloep | Crooked Sailors' Guild (Port Royal) Limited | enrolled at Chamber of Port Royal | 70 |
| Norther (NSG-21) | hull, sloep | Crooked Sailors' Guild (Port Royal) Limited | enrolled at Chamber of Port Royal | 70 |
| La Rafale (NSG-22) | hull, sloep | Guilde des Navigateurs Obliques de Sainte-Marie SARL | enrolled at Chambre de Sainte-Marie | 70 |
| Angin Ribut (NSG-23) | hull, sloep | PT Gilda Pelayar Serong Ambon | enrolled at Kamar Ambon | 70 |
| De Bode (NSG-24) | hull, galjoot | Neederlandsch Schuijnvaerders Gilde N.V. | enrolled at Kamer Vlissingen | 15 |
| An Teachtaire (NSG-25) | hull, galjoot | Crooked Sailors' Guild of Baltimore Limited | enrolled at Chamber of Baltimore | 15 |

### Muster by chamber

| Chamber | Legal entity | Hulls | Seagoing hands | Shore hands | All hands |
| --- | --- | --- | --- | --- | --- |
| Kamer Vlissingen | Neederlandsch Schuijnvaerders Gilde N.V. | 8 | 819 | 120 | 939 |
| Chamber of Baltimore | Crooked Sailors' Guild of Baltimore Limited | 4 | 193 | 45 | 238 |
| Chamber of Port Royal | Crooked Sailors' Guild (Port Royal) Limited | 5 | 338 | 70 | 408 |
| Chambre de Sainte-Marie | Guilde des Navigateurs Obliques de Sainte-Marie SARL | 3 | 178 | 50 | 228 |
| Kamar Ambon | PT Gilda Pelayar Serong Ambon | 5 | 416 | 65 | 481 |
| **All** | | **25** | **1,944** | **350** | **2,294** |

The fleet of 25 wooden ships an' the 5 chambers of operation together carry 1,944 seagoing
hands an' 350 hands ashore: 2,294 souls all told, which the Gilde rounds to about 2,300
when speakin' an' never when reportin'.

## 4. Who holds which role

Offices hold the roles; the officers who held them in FY2025 be these, with their bios in
[the people](../lore/people.md). A role be granted per entity, so a Harbourmaster sees
their own chamber an' the Quartermaster-General sees all.

| Office | Officer, FY2025 | Chamber key |
| --- | --- | --- |
| Captain-General | Ezekiel Brathwaite | port_royal |
| Presiding Lord of De Heeren Vijf | Anneke Roozemond | vlissingen |
| Quartermaster-General | Saoirse Ní Dhrisceoil | baltimore |
| Advocaat-Boekhouder | Marijke van der Goes | vlissingen |
| Harbourmaster | Joost Wisse | vlissingen |
| Harbourmaster | Dónal Crowley | baltimore |
| Harbourmaster | Icylin Samuda | port_royal |
| Harbourmaster | Voahangy Rasoanaivo | sainte_marie |
| Harbourmaster | Yusuf Tuhumury | ambon |
| Sailing Master | Andi Nurhaida | ambon |

| Platform role | Held by | Scope |
| --- | --- | --- |
| Organization administrator | Advocaat-Boekhouder | all entities |
| DMA owner (double materiality) | Quartermaster-General | all entities |
| E1 read & write | Advocaat-Boekhouder; each chamber's Harbourmaster for their hulls | per entity |
| E2, E3, E4, E5 read & write | Quartermaster-General; Harbourmasters for their chamber | per entity |
| S1 read & write | Quartermaster-General (keeper o' the muster an' the Matanzas schedule) | all entities |
| S2, S3, S4 read & write | Harbourmasters for their ports; Quartermaster-General consolidates | per entity |
| G1 read & write | Advocaat-Boekhouder (registrar o' commissions an' bonds) with the Prize Council's clerk | root entity |
| ESRS 2 narrative | Advocaat-Boekhouder drafts; Captain-General approves | root entity |
| Survey respondent | Harbourmasters (one per chamber) an' the master o' each hull | per location |
| Read-only, approvers o' the reckonin' | Captain-General; presiding Lord o' De Heeren Vijf | all entities |
| Reduction plan | Quartermaster-General with the Sailing Master | all entities |

## 5. Surveys an' the muster o' questions

The platform's survey machinery (schema, deployment, assignment, answer, evidence) maps
onto the Gilde's oldest habit: the Kermis muster, when every hull's master answers the
Quartermaster's questions for the year. One deployment per Kermis year; one assignment per
hull location an' one per base; answers written by the master or Harbourmaster in the
internal register; evidence as listed below.

## 6. Evidence a 1600s company can attach

| Evidence kind | What it be | Where it comes from |
| --- | --- | --- |
| Ledger page | The boekhouder's tally o' wood, tar, powder, oil an' provisions per hull an' voyage | each chamber's counting house |
| Logbook leaf | Daily log: position by dead reckonin', weather, watches, hurts, punishments, cargo worked | each hull's master |
| Gunner's book | Powder an' shot expended, by date an' cause (signal, exercise, service) | each hull's gunner |
| Muster roll | Hands aboard by name, office, share, chamber o' origin, age attested | Quartermaster-General |
| Matanzas schedule payments | Hurts taken an' sums paid, by hand an' date | Quartermaster-General |
| Commissie register | Letters o' marque, bonds, interrogatories, Prize Council sentences | Prize Council, Middelburg |
| Notary's count | A notary's attestation o' hulls, hands an' turnover at the Kermis | Middelburg notary |
| Careenin' record | Dates hauled down, timber an' tar used, hull condition | each chamber's hard |

All evidence be ink on paper. It reaches the platform as described next.

## 7. The landsmen's exception: paper to platform

The Gilde's own hands touch no machine. At each Kermis the chambers' ledgers come to
Middelburg by galjoot. There a notary's clerk — a landsman employed under the landsmen's
exception in the articles — keys the tallies into the platform's activity-data upload (a
spreadsheet by the platform's word, a fair copy o' the ledger by ours), enters the survey
answers as dictated, an' attaches the evidence as scanned pages. The words be the Gilde's;
the keys be the clerk's. The Advocaat-Boekhouder reads every entry back against the ledger
afore it be marked final, an' signs the notary's count.

## 8. Checks an agent must make afore answerin'

1. The entity name be spelled exactly as in section 2.
2. The period key be `102024-092025` for this reckonin' an' `102023-092024` for the year measured from.
3. A number quoted appears in [canon](../canon/facts.yaml) or in a `data/` file; if not, mark it `[UNCHARTED]`.
4. A hull named exists in [the fleet register](../data/fleet.csv); a base in [the bases register](../data/bases.csv).
5. The register be formal for anythin' the platform will show a regulator.

## Related

- [The five chambers](../lore/bases.md) an' [the fleet](../lore/fleet.md)
- [Governance](../lore/governance.md) an' [the people](../lore/people.md)
- [ESRS 2 general disclosures](esrs2-general.md)
- [The reportin' playbook](../agents/reporting-playbook.md)
- [Canon](../canon/facts.yaml)
