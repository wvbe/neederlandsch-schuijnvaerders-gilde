---
title: Operations — routes, cargo, the Division, shares an' seasons
status: draft
last-verified: 2026-09-18
canon-refs:
  - scale.fleet_count
  - scale.base_count
  - scale.seagoing_headcount
  - scale.preferred_cargo
  - reporting.reported_year_key
  - reporting.fiscal_year_name
  - company.prize_council_seat
  - operations.interdiction_service_name
  - operations.interdiction_steps
  - operations.refusal_conditions
  - operations.technology_rule
  - operations.share_split_prize_percent.client
  - operations.share_split_freight_percent.company
  - operations.commissions_served_fy2025.total
---

# Operations — routes, cargo, the Division, shares an' seasons

The Neederlandsch Schuijnvaerders Gilde N.V. carries spices, valuables and exotic materials
between the seven waters it sails — the Netherlands, the United Kingdom, Ireland, the
Caribbean, the Indian Ocean, South East Asia and the Pacific islands — in a fleet of 25
wooden ships worked out of 5 chambers of operation and crewed by 1,944 seagoing hands. It
carries them under sail alone, on the seasons the winds allow and not on a day of our
choosing, and beside them it carries a contracted interdiction service, the Letters of
Marque Division, which stops and examines vessels under a client's registered commission.
Every hull named below stands on the register in [`../data/fleet.csv`](../data/fleet.csv).

## Routes

Seven standing routes carry the trade. Passage times are the median of the last ten seasons.

| route code | from | to | season sailed | typical passage in days | cargo outbound | cargo homeward | hulls assigned |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ATL-1 | Vlissingen | Port Royal (via Baltimore) | December to May; never into the hurricane season, June to November | 48 | cordage, canvas, tar, iron, biscuit, coin under seal | see ATL-2 | NSG-02, NSG-13, NSG-05, NSG-06 |
| ATL-2 | Port Royal | Vlissingen (via Baltimore) | Homeward from March; clear of the Caribbean before 1 June | 55 | see ATL-1 | logwood, cochineal, indigo, cacao, condemned prize goods | NSG-02, NSG-08, NSG-13, NSG-06 |
| IND-1 | Vlissingen | Île Sainte-Marie (via the Cape of Good Hope) | Out October to January; the easting run down in the Roaring Forties, the westerlies between 40 and 50 degrees south | 95 | canvas, iron, cordage, bar silver under seal | see IND-3 | NSG-01, NSG-03 |
| IND-2 | Île Sainte-Marie | Ambon | Eastbound on the south-west monsoon, May to September | 55 | canvas for the sail loft, iron, rice | see IND-3 | NSG-01, NSG-03, NSG-18, NSG-09 |
| PAC-1 | Ambon | the Bismarck Archipelago, the Solomon Islands, the Caroline Islands and Fiji | April to October on the south-east trades; home before the South Pacific cyclone season, November to April | 90 | iron, canvas, salt, letters | sandalwood under the grower's mark, pearl shell, gum copal | NSG-10, NSG-04 |
| IND-3 | Ambon | Vlissingen (via Sainte-Marie and the Cape) | Westbound on the north-east monsoon, October to March; the Cape rounded before the southern winter | 150 | see IND-1 | cloves, nutmeg, mace, cinnamon, vanilla, pearls | NSG-01, NSG-03, NSG-04, NSG-18 |
| CST-1 | Baltimore | Vlissingen (via the Irish Sea and the Channel) | All year; thinnest November to February | 12 | salt beef, biscuit, casks, letters | letters, chambers' totals, chandlery | NSG-25, NSG-14, NSG-24, NSG-06 |

**On the seasons, plainly.** The Atlantic hurricane season runs June to November and peaks
in September, so ATL-1 and ATL-2 are sailed round it: a retourschip caught on that coast in
September is a loss waiting for a date. In the Indian Ocean the north-east
monsoon blows October to March and the south-west monsoon May to September, and the Ambon
run is bound to them absolutely — IND-2 east on the south-west, IND-3 west on the
north-east. The southern leg of IND-1 rides the Roaring Forties, the fastest water the
Gilde has and the worst, where the articles require two hands on the whipstaff and a life
line rigged fore and aft. The fluyts NSG-11 and NSG-12 keep a separate Baltic run, April
to October, for the yard's oak, hemp and tar.

**Route notes, from the log.** ATL-1 be the easy one an' the one that kills ye: 600 nmi to
Baltimore be a shakedown, then 3,700 nmi where a sprung seam be yer own business. IND-1 be
near 6,500 nmi out o' sight o' land, an' the hands call the Forties "the free ride ye pay
for after". PAC-1 be reef water an' poor charts. CST-1 be the humblest run on the books an'
the one the reckonin' depends on: it carries the chambers' totals to Middelburg.

## Cargo

The Gilde takes low volume and high value: spices, valuables and exotic materials, and
nothing else.

**Spices.** Cloves, nutmeg and mace from Ambon, Banda and Ternate; cinnamon, pepper,
vanilla. The risk is that a cask of nutmeg is worth more than the fluyt beneath it and
weighs nothing, so it walks, and that spice is ruined by water, heat and any smell it sits
beside. Stowed in the 'tween decks on dunnage of split rattan and matting, clear of the
bilge, in double sacks within sealed casks, never within two frames of tar, hides or fish.
Each cask carries the chamber's device in wax and a tally number, and none is opened at sea
but for fire.

**Valuables.** Bar silver and coin under seal, cochineal, indigo, pearls, plate and bills
of exchange. The risk is that everybody aboard and ashore knows what it is worth and some
of them are a month's wages short. Stowed in the strongroom, a cask-lined hold under the
great cabin with three locks and three keyholders — the captain, the Quartermaster and the
client's agent — opened only in daylight, in harbour, with all three present.

**Exotic materials.** Sandalwood under the grower's mark, pearl shell, camphor, gum copal,
beeswax, logwood, and found ambergris — gathered from a beach, never taken from a whale.
The risk is that this trade is thick with theft and false provenance, and one wrongly
papered bale can condemn a whole cargo. Stowed dry and ventilated, the papers travelling in
the ship's strongbox, not with the goods.

**Guarding a wooden hull.** Fire is the true enemy of all three classes. No naked flame
goes below: light in the hold is a horn lanthorn on a hook, the galley fire is drawn at
sunset in a seaway, and the magazine sits apart behind a felt-curtained door, opened by the
gunner alone. An anchor watch is kept in every port, and bulk is broken only against a
written order.

### What we will not carry

- **Protected species and materials.** No ivory, rhino horn, pangolin, shark fin, live
  coral or reef stone, wild-taken timber of a listed species, or newly taken sea-turtle
  shell. The awkward part first: the Port Royal warehouse still holds old tortoiseshell of
  documented provenance, bought long before the standing order. The chamber will not trade
  it, and no new shell has come aboard a Gilde hull in living memory.
- **People.** In no condition and under no name: cargo, passenger under duress, indentured
  hand, prisoner or prize. This is the Sainte-Marie clause, dated 1697 and named for the
  island where the lesson was learned, and it forbids pressing and any dealing in persons.
- **Arms to either side of a war.** No powder, shot, small arms or guns as freight, to any
  party, in any quarrel. The Gilde carries powder for its own guns and no one else's.
- **Anything else the articles bar.** Unprovenanced antiquities; goods under sanction;
  cargo whose papers we cannot read; any cargo the Quartermaster may not inspect before it
  is stowed.

## The Letters of Marque Division

The Letters of Marque Division is the Gilde's contracted interdiction service. It does not
sail on its own account and it does not hunt. It acts only on a client's commission, under
a written procedure of 5 steps, from commission to condemnation, tested file by file by the
Prize Council at Middelburg.

1. **Commission and bond.** The client's letter of marque is registered at the Middelburg
   chamber and a bond posted there before any hull sails. An unregistered commission is no
   commission, and a hull sailing on one is in mutiny, not in business.
2. **Papers and crew examined.** The mark is stopped and boarded, and her papers and crew
   examined aboard under a written interrogatory — the same questions in the same order in
   every ocean — the answers signed by the examining officer and the master examined.
3. **Sealed and brought in.** Seized cargo is sealed where it lies and brought to the
   nearest chamber without breaking bulk: no hatch opened, no sample drawn, nothing sold or
   taken.
4. **Adjudication.** The Prize Council at Middelburg rules good prize or orders
   restitution. Where a seizure fails, restitution is made in full and the costs fall on
   the client, not on the vessel stopped.
5. **Sale or release.** A prize ruled good is sold at open auction, under the bell, with
   the Advocaat-Boekhouder's clerk at the table; or the vessel is released against a
   written ransom bill, which is a bond and nothing else. It secures a debt on paper, never
   a person.

**What the Division refuses.** These 8 conditions bind every hull and officer, and no
client may buy an exception:

1. No seizure of vessels of the Netherlands, the EU, or the client's declared allies.
2. No commission from a client at war with the Netherlands, and none against a party under
   truce.
3. No breaking bulk or sale before adjudication.
4. No seizure without inspection of papers; clean papers means release, costs to client.
5. No operations outside the waters or term named in the commission.
6. No pressing of captured crew into service.
7. No hostage-taking to secure a ransom bill; ransom is a bond only.
8. No attack under a flag of truce or in a neutral harbour.

**How a seizure is effected, and what it cost.** No hand of the Gilde and no hand of any
seized vessel was killed or gravely hurt in the reporting year 102024-092025. Seizures are
effected by boarding under superior sail and superior numbers with weapons shown and not
used: the sloop comes up where the mark cannot run, the boarding party goes across with
cutlasses sheathed and muskets slung, and the guns speak only as a signal to heave to,
never into a hull. Where the mark will not stop, the Division breaks off and reports it.
The Division served 9 commissions in the reporting year: 5 ended in good prize, of which 4
were sold at auction and 1 released against a ransom bill; 2 ended in restitution ordered
by the Prize Council at the client's cost; and 2 ended in release on the spot, the papers
being clean, again at the client's cost. The sloops NSG-19 to NSG-23 do this work, with
NSG-07 and NSG-09 stopping a mark where a sloop is not to hand.

## Shares

Every voyage is divided the same way, in the open, at the chamber that fitted her out, in EUR.

| what is divided | client | company | chamber fee | crew |
| --- | --- | --- | --- | --- |
| a prize, net of costs | 40 | 30 | 10 | 20 |
| a freight, net of costs | 0 | 60 | 15 | 25 |

On a prize the client takes the larger part, because it is his commission, his bond and
his risk of costs when a seizure fails. On a freight he takes nothing, having taken his
goods instead and paid his freight already; the 0 is an accounting, not a slight.

**How a share is computed and paid.** Costs come off first: victuals, powder, port dues,
pilotage and the Prize Council's fee. What remains is divided by the table above. The crew
part is split between the hulls that took part in proportion to each hull's parten share on
the register — 1/16 for a retourschip or a fluyt, 1/8 for a jacht or a galjoot, 3/16 for an
interdiction sloop — and within each hull by the ladder in the articles: one share to a
hand, more to the skilled and the officers, one share to the common chest. Payment is made
at the chamber counting house within thirty days of the auction or of the Prize Council's
sentence, whichever falls later, against the hand's mark in the pay ledger.

**The floor under "no prey, no pay".** The old rule was that a hand who took nothing was
paid nothing, and the Gilde does not pretend that rule was kind. It no longer stands alone.
Every enrolled hand has a guaranteed floor: full victuals and water aboard, a berth and
lodging ashore at the chamber between voyages, the surgeon's attendance, and passage home
from wherever the voyage ends, prize or no prize. A monthly floor payment is set each
Kermis by the Council and recorded in the articles. On top of it the hardship chest, kept
by the Quartermaster-General, pays the Matanzas schedule to a hand hurt in the Gilde's
service and maintains a hand sick, disabled or waiting out a lost hull. The share system is
still a risk to a hand's income, and it is reported as one under S1.

## Seasons an' the Kermis year

The Kermis year runs 1 October to 30 September, and that is the shape of the sailing, not
an accounting convenience. October finds the Atlantic hurricane season closing, the
north-east monsoon making up in the Indian Ocean, and the outbound retourschepen fitting
for the Cape. The year opens with the fleet in hand and closes with it in hand: the last
homeward run is in before the end of September, the totals go up the Schelde by galjoot,
and the books shut on the 30th with no hull unaccounted for. A December year-end would
close the books in the middle of the Atlantic, and the Council has never seen the sense in it.

Each hull is breamed quarterly where she lies. The full careen, hove down on her side, is
once a year at her own chamber:

| chamber | careening months | why then |
| --- | --- | --- |
| Kamer Vlissingen | October | the Kermis month, on the Schelde mud at low water, outside the seal breeding season |
| Chamber of Baltimore | February to March | the Atlantic run is at home and the grey seals have whelped |
| Chamber of Port Royal | April to May | afloat again before 1 June; no hull on the hard in hurricane season |
| Chambre de Sainte-Marie | May to June | after the cyclone season, before the whales come in to calve in July |
| Kamar Ambon | October to November | the westbound retourschip has gone, the north-west monsoon not yet in |

## Gear an' means

The standing order is short. *Nothing aboard or ashore that was not in use on a Dutch ship in the 1600s.* Here be the inventory.

- **Hull and rig.** Oak frames and planking, pine masts and spars, treenails and iron
  bolts, oakum and pitch, hemp cordage tarred with Stockholm tar, linen or hemp sailcloth
  cut at the Ambon loft, tallow and sulphur on the bottom, lead sheathing where the shipworm
  is worst. Nothing later than that.
- **Navigation.** Magnetic compass in a gimballed box, cross-staff and backstaff, lead line
  armed with tallow, log line and chip log, sandglasses of the half hour and the log glass,
  traverse board and dead reckoning, portolan and Mercator charts and the Van Keulen house's
  pilots. Latitude we have; longitude we reckon, and we tell clients and regulators plainly
  that a reckoned longitude is an estimate carrying real risk.
- **Communication.** Flags by a short written code, lanterns by night, guns as signals and
  salutes, and the packet by galjoot — NSG-24 and NSG-25. The speed of the post is the speed
  of the wind, and the reporting calendar is built around that.
- **Record keeping.** Ink on paper, quill and graphite pencil, double-entry ledgers per
  chamber and per hull, the gunner's book for every pound of powder burnt, bills of exchange
  and wax seals. Every ledger is copied to Vlissingen twice a year, a standing order the
  Port Royal earthquake of 1692 wrote for us.
- **Light and heat.** Tallow candles, whale oil and lamp oil in lanthorns, galley wood and
  charcoal. This is the whole of the Gilde's Scope 1 story, tallied per hull and chamber in
  the boekhouder's ledger.
- **Weapons.** Muzzle-loading cannon of bronze and cast iron on wooden carriages, matchlock
  and flintlock muskets, cutlass, pike and boarding axe. Shown, not used. Powder is handled
  by grown hands only.
- **Medicine.** A surgeon aboard every hull of 70 hands or more, a surgeon's mate on
  NSG-03, a chest of saws, probes, cautery and laudanum, citrus and fresh food at every
  chamber. A hurt taken in the Gilde's service is compensated on the Matanzas schedule,
  named for the founding prize of 1628 and paid from the hardship chest.

**How the ledgers reach the Salacia platform.** The tallies are gathered to Middelburg by
galjoot at the Kermis closing, in ink, on paper, sworn. There a notary's clerk — a landsman,
not a hand of the Gilde — conveys them into the Salacia platform under the landsmen's
exception in the articles. The Gilde's own hands touch none of it, and we say so plainly.
The words in the platform are ours; the means of getting them there are a landsman's, and
he is paid for it like any other chandler.

## Related

- [Backstory and timeline](backstory.md) — why the Gilde sails as it does
- [The fleet](fleet.md) — the hulls named above
- [The five chambers](bases.md) — where the routes begin and end
- [Articles of agreement](articles-of-agreement.md) — the share ladder and the Sainte-Marie clause
- [Fleet register](../data/fleet.csv) — the hull marks
- [Canon](../canon/facts.yaml) — the numbers an' names
