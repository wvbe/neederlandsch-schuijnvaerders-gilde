# Decisions on the open questions

Resolved 2026-09-18 jointly by the planning agent and an advisory agent briefed as a
historian of 17th-century piracy, privateering and Dutch maritime trade. Each entry gives
the decision, the historical grounding, the platform or regulatory constraint it had to
satisfy, and the alternative rejected. These values go into `canon/facts.yaml` in Task 1
and are binding for every later task unless changed here first.

## 1. Legal form, seat, founding year

**Decision.** Dutch N.V. with statutory seat in **Vlissingen**. The company's internal
Prize Council and audit chamber sit in **Middelburg**. Founded **1621**, articles dated to
the lapse of the Twelve Years' Truce (9 April 1621), weeks before the WIC charter of
3 June 1621. The backstory (Task 5) must explain the conversion of a 1621 rederij into a
modern N.V. (a 19th- or 20th-century re-incorporation under Dutch company law) so that an
EU legal entity exists for CSRD.

**Grounding.** Vlissingen was the Republic's privateering town: its captains raided
Spanish America around 1600, it was an English Cautionary Town 1585–1616, and Michiel de
Ruyter was born there in 1607. Middelburg housed the Zeeland Admiralty college and the
Zeeland chambers of the VOC and WIC, and hosted the Heeren XVII two years in every eight.
The pairing mirrors the real Zeeland split between the sea-town that outfitted privateers
and the administrative town that condemned their prizes. 1621 is when privateering resumed
at scale and the state-sanctioned raiding company was chartered; PSI turns 405 in 2026.

**Constraint satisfied.** A Dutch N.V. is a large undertaking under CSRD; Salacia needs one
organization name and one root legal entity.

**Rejected.** Hoorn or Enkhuizen: small chamber shares, no privateering culture, and 1602
(VOC founding) reads as "monopoly trader", not "licensed raider".

## 2. Fiscal year

**Decision.** **1 October to 30 September**, called the Kermis year. Reported year is
FY2025 (1 Oct 2024 to 30 Sep 2025), Salacia key `102024-092025`. Base year FY2024, key
`102023-092024`. Reporting-year start month in Salacia: 10.

**Grounding.** The VOC sailed three named outbound fleets: the Kermisvloot in September
(formalised 1636), the Kerstvloot around the turn of the year and the Paasvloot in spring;
return fleets were normally home in the Texel roads by July and sold at the autumn
auctions. Closing at 30 September therefore follows the year's returns being landed and
sold. It also fits the other theatres: the Atlantic hurricane season is winding down, the
Indian Ocean north-east monsoon opens in October, and the West Cork pirate fleets wintered
away and returned in spring. October was the quiet accounts-and-careening month everywhere
PSI trades.

**Constraint satisfied.** Salacia derives the period key from the organization's start
month, so a non-calendar year is supported and is in fact a useful demo of that feature.
CSRD reporting follows the financial year, so no conflict.

**Rejected.** 1 September (the fleet's actual departure): sits at hurricane peak and puts
year-end in the middle of the auction season.

## 3. Reporting currency

**Decision.** **EUR** is the only currency in any figure that reaches Salacia or a metric
table. A secondary flavour column in **Dutch guilders of 20 stuivers** may appear in
prose-only tables and in lore. "Pieces of eight" and "rijksdaalders" are the cash-in-hand
vocabulary of ships and bases, never a reported value. Indian Ocean bases carry an "Asian
agio" note when converting, as lore colour.

**Grounding.** VOC, WIC and Admiralty books were kept in money of account: guilders,
stuivers (20 to the guilder) and penningen (16 to the stuiver), though most coin in hand
was Spanish silver. The VOC fixed its accounting guilder to the 1608 rijksdaalder at 48
stuivers, while from 1640 it rated the rijksdaalder and the real de a ocho at 60 stuivers
in Asia to stop coin draining east: the "light money / heavy money" gap of about a fifth.

**Constraint satisfied.** CSRD thresholds and financial datapoints are in EUR; a second
currency in a quantitative datapoint would break Salacia parsing.

**Rejected.** Pieces of eight as the primary unit: no Dutch counting house kept books in a
foreign coin, and Spanish dollars were valued differently in every port.

## 4. Ships as Salacia locations; ownership model

**Decision.** Hulls are **company-owned**, each enrolled at one of the five chambers
(bases) and modelled in Salacia as a **location under that chamber's legal entity**. As a
heritage twist, each ship's crew collectively holds a minority "parten" interest in her,
paid out as the buccaneer share. This is the bridge between the pirate share system and a
single reportable undertaking.

**Grounding.** Dutch merchant shipping ran on the partenrederij: a ship divided into
1/8 to 1/64 shares held by merchants, skipper and shipwright, managed by a boekhouder who
kept the voyage account. The VOC and WIC instead owned hulls outright, built them in their
own yards (Amsterdam Oostenburg, Middelburg) and assigned each to a chamber that equipped
and manned it in charter proportions. Buccaneer vessels were owned by the captain or a Port
Royal or Tortuga syndicate on "no prey, no pay" under a chasse-partie.

**Constraint satisfied.** Salacia's model is legal entity → location; E1 activity data and
S1 headcount can then be captured per ship and rolled up per base.

**Rejected.** Per-voyage partenrederij: 25 part-owned ventures with rotating owners, the
fragmentation the VOC charter existed to end, and unreportable as one undertaking.

## 5. Interdiction business framing

**Decision.** A five-step **commission-to-condemnation** procedure, written into
`lore/operations.md` (Task 9) and tested in `csrd/g1-conduct.md` (Task 18):

1. The client's letter of marque is registered at the Middelburg chamber and a **bond**
   is posted.
2. The target is stopped; its **papers and crew are examined** aboard with a written
   interrogatory.
3. Seized cargo is sealed and brought to the nearest PSI base **without breaking bulk**.
4. The internal **Prize Council** adjudicates "good prize" or orders restitution; costs of
   a failed seizure fall on the client.
5. The prize is sold at open **auction** or released against a written **ransom bill**;
   shares go to client, company, chamber fee and crew.

**Refusal conditions** (final wording in Task 9):

1. No seizure of vessels of the Netherlands, the EU, or the client's declared allies.
2. No commission from a client at war with the Netherlands, and none against a party
   under truce.
3. No breaking bulk or sale before adjudication.
4. No seizure without inspection of papers; clean papers means release, costs to client.
5. No operations outside the waters or term named in the commission.
6. No pressing of captured crew into service.
7. No hostage-taking to secure a ransom bill; ransom is a bond only.
8. No attack under a flag of truce or in a neutral harbour.

**Grounding.** From the 1597 Admiralty instruction, Dutch commissievaarders needed a
commission issued in the Stadholder's name by one of the five Admiralty colleges and had to
post a bond; the Admiralty adjudicated prizes, released those not judged good prize, and
made sponsors pay costs. English privateers likewise gave bonds and had prizes condemned in
the High Court of Admiralty, which examined papers and interrogated crews under standing
interrogatories and forbade breaking bulk before sentence. Ransom bills were routine until
Britain banned them in 1782. Jamaica's Governor Modyford issued anti-Spanish commissions to
Morgan's buccaneers until the Treaty of Madrid (1670). The share-out follows the WIC
pattern of its 1623–36 campaign, including Piet Heyn's silver fleet at Matanzas (1628).

**Constraint satisfied.** Architecture decision 7 (no lethal violence in the reporting
period, no forced labour) and a G1 due-diligence procedure an auditor could test.

**Rejected.** Framing interdiction as "reprisal" for the client's own losses: a
late-medieval form superseded by state commissions by 1600, and it invites justifying
violence.

## 6. Headcount, fleet mix, turnover

**Decision.** Fleet of 25 with seagoing crew of **1,944** and shore staff of about
**350**, total about **2,300**. Turnover about **EUR 480M**.

| Type | Count | Crew each | Crew total | Role |
| --- | --- | --- | --- | --- |
| Retourschip / East Indiaman | 4 | 220 | 880 | Long-haul cargo, valuables |
| Jacht / light frigate | 6 | 90 | 540 | Escort, fast cargo, interdiction |
| Fluyt | 8 | 18 | 144 | Bulk spices and materials |
| Interdiction sloop / bark | 5 | 70 | 350 | Boarding and seizure |
| Galjoot / advice boat | 2 | 15 | 30 | Dispatches, coastal supply |
| **Total** | **25** | | **1,944** | |

**Grounding.** A VOC retourschip of 600–1,000 tons sailed with 200–300 men including
soldiers; a jacht of 100–300 tons carried 40–80; the fluyt was famous for 12–20 men on
300–500 tons; buccaneer sloops carried 50–120 for boarding. A single VOC return cargo could
be worth several hundred thousand guilders, and Heyn's 1628 silver fleet about 11.5 million.
EUR 480M is about EUR 210k per head, in range for high-value specialist logistics plus
maritime security, provided the story stresses low-volume high-value cargo (spices,
bullion, dyestuffs, tortoiseshell, ambergris) plus interdiction fees and prize shares.

**Constraint satisfied.** Above the revised CSRD large-undertaking thresholds (over 1,000
employees and over EUR 450M net turnover as agreed in the Omnibus negotiations; Task 1
verifies the current values and records them with the date checked).

**Rejected.** A fleet of mostly fluyts: 25 of them crew about 450, cannot board anything,
and leave PSI under the headcount threshold.

## 7. Bases and languages of legal entity names

**Decision.** One chamber per region, each a real 1600s haven with a documented
commissioning or supply economy:

| Region | Base | Entity language | Historical hook |
| --- | --- | --- | --- |
| Netherlands | Vlissingen (seat) | Dutch | Privateering town, Cautionary Town 1585–1616, De Ruyter |
| UK / Ireland | Baltimore, West Cork | English and Irish (Dún na Séad) | With Leamcon and Crookhaven the North Atlantic pirate headquarters c. 1605–15; sacked 20 June 1631 by Algerine corsairs under Murat Reis the Younger (Jan Janszoon of Haarlem). Keeps the base inside the EU |
| Caribbean | Port Royal, Jamaica | English | Buccaneer capital 1655–92, Modyford's commissions, Morgan, Treaty of Madrid 1670, earthquake 7 June 1692 |
| Indian Ocean | Île Sainte-Marie (Nosy Boraha), Madagascar | Malagasy and French | Adam Baldridge's fortified post from 1691, supplied from New York by Frederick Philipse; the pirate round's victualling point until the 1697 uprising |
| South East Asia / Pacific | Ambon | Indonesian (PT form) | VOC seat in the Moluccas from 1605, the clove monopoly, the 1623 Ambon affair; gateway to Banda, Ternate and the Pacific |

Every entity name is shown with an English gloss. Exact names are set in Task 6.

**Constraint satisfied.** Five legal entities under one root, one per region cluster;
locations for CSRD site-level disclosures; local community and biodiversity hooks for
S3 and E4.

**Rejected.** Jolo in the Sulu Sea: the Iranun and Balangingi raiding system peaked
1770s–1840s and was built on slave raiding, which clashes with the guardrails. Tortuga is
a fine French-language substitute for Port Royal if a Francophone base is ever wanted.

## 8. Governance and signatories

**Decision.** Two-tier governance blending the pirate council with the Dutch chamber model:

- **De Heeren Vijf (the Lords Five):** supervisory tier, one bewindhebber per chamber,
  presidency rotating (Vlissingen three years, each other chamber one year).
- **Raad van Kapiteins (Council of Captains):** management board of captains elected by
  their ships' councils, presided over by an elected **Captain-General**.
- **Quartermaster-General:** elected by all crews, keeper of the common chest, veto on
  distributions. The crews' counterweight and the natural sustainability and
  whistleblowing officer.
- **Advocaat-Boekhouder:** company secretary and chief bookkeeper; attests the figures.

**Signatories of the sustainability statement:** the Captain-General for the Council of
Captains and the presiding Lord of the Heeren Vijf, countersigned by the
Quartermaster-General, with the Advocaat-Boekhouder attesting the figures.

**Grounding.** Pirate ships elected their captain, whose authority was unquestioned only
in chase and battle, and a quartermaster as the crew's trustee for shares and discipline,
with the whole company as council (Exquemelin; Johnson's General History; Roberts'
articles). Buccaneer expeditions such as Morgan's 1670 Panama fleet were governed by a
council of captains under written articles. The VOC ran on chamber bewindhebbers sending
delegates to the Heeren XVII, with hoofdparticipanten given oversight after the 1623
reforms and a permanent Advocaat drafting resolutions.

**Constraint satisfied.** Dutch practice under CSRD has both management and supervisory
boards sign the management report; ESRS 2 GOV-1 to GOV-5 need named bodies with roles.

**Rejected.** A single seventeen-seat board in the Heeren XVII style: removes the elected
counterweight that makes the company piratical and is unwieldy for five chambers.

## Additional historical hooks to weave in (Tasks 3, 5, 8, 18)

- Piet Heyn's silver fleet at Matanzas Bay, 8 September 1628, as the "founding prize".
- The Dutch and English Prize Papers as the model for PSI's evidence archive: papers and
  interrogatories per seizure become the survey evidence files.
- Claes Compaen of Oostzaan, privateer turned pirate, pardoned 1627: the cautionary tale
  in the code of conduct.
- The Sainte-Marie uprising of 1697 as the origin of the "no forced labour, no slave
  dealing" clause.
- Henry Every's 1695 seizure of the Ganj-i-Sawai and the East India Company crisis as the
  reason PSI refuses to touch pilgrim or sovereign vessels.
- The 1692 Port Royal earthquake for the base's "rebuilt on the spit" story and a
  disaster-risk disclosure.
- The Batavian Crown coinage of 1645 (48, 24, 12 stuivers) as the internal payslip unit.
- Henry Mainwaring's 1618 treatise calling Ireland "the nursery and storehouse of pirates".

## Sources the advisory drew on

- Lunsford, V., *Piracy and Privateering in the Golden Age Netherlands* (Palgrave),
  chapter "Kapers and Commissievaarders".
- Verhees-van Meer, J.Th.H., *De Zeeuwse Kaapvaart tijdens de Spaanse Successieoorlog
  1702–1713* (Middelburg, 1986).
- Heeren XVII structure and rotation: encyclopedia.com entry "Heeren XVII".
- Netherlands Indies gulden, light/heavy money, 1640 revaluation; Dutch rijksdaalder
  (Wikipedia).
- VOC named fleets: aronson.com "VOC Asian trading routes".
- WIC 1623–36 captures: encyclopedia.com "Dutch West India Company"; Wikipedia.
- Adam Baldridge, Pirate Round, Sainte-Marie pirate massacre 1697 (Wikipedia).
- Sack of Baltimore; Jan Janszoon; Breen, "Pirate Ports and Harbours of West Cork",
  *Journal of Maritime Archaeology*; Dictionary of Irish Biography, Sir William Hull.
- Dutch Admiralties and prize jurisdiction: Wikipedia; Rozenberg Quarterly, "Dutch Prize
  Papers".
- Exquemelin, *De Americaensche Zee-Roovers* (1678); C. Johnson, *A General History of the
  Pyrates* (1724); Gaastra, *The Dutch East India Company*; Rediker, *Villains of All
  Nations*; Earle, *The Pirate Wars*.

**Known uncertainty.** The size of Dutch privateer bonds and the Admiralty's exact
percentage of prizes were not verified; the mechanism is described without figures. Task 3
should confirm or tag these as invented.
