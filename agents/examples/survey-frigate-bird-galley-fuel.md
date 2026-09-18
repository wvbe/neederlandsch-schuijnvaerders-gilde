---
title: "Example — survey answer for a hull (internal register)"
status: draft
last-verified: 2026-09-18
register: internal
request: "Kermis muster survey, assignment to location The Frigate Bird (NSG-07), question on fuel burned aboard, period 102024-092025"
sources: [csrd/salacia-mapping.md §3 and §6, data/e1-activity-data.csv, data/fleet.csv, lore/people.md]
canon-refs: [reporting.reported_year_key, "bases[key=port_royal].entity_name"]
---

# Example — survey answer, The Frigate Bird

**Request.** The Kermis muster o' questions be deployed to every hull. The assignment for
*The Frigate Bird* asks: state the fuel burned aboard in the period, by kind an' quantity,
with evidence.

**Answer as submitted**

```text
Location: The Frigate Bird (NSG-07) — Legal entity: Crooked Sailors' Guild (Port Royal) Limited — Period: 102024-092025
Answered by: Captain-General, Ezekiel Brathwaite, who holds this hull

Q3. State the fuel burned aboard in the period, by kind an' quantity.
A. Four kinds, an' nothin' else. Firewood for the galley, 9,590 kg. Charcoal for the same
galley on the long passages, 1,865 kg. Whale oil for the lamps, 460 litre — more than I
like, an' the fish oil we trialled at Port Royal smoked worse, so the figure stands for
this year an' I'll not dress it up. Black powder, 355 kg, all of it signals an' exercise;
not a charge fired in anger, as the gunner's book shows page by page. No oil for any wheel,
no coal, no gear that would want either: she be a jacht o' 90 hands an' sails as her
grandmothers did.
Evidence: boekhouder's ledger, Chamber of Port Royal counting house, 1 October 2024 to
30 September 2025, The Frigate Bird's page (wood, charcoal, oil); gunner's book NSG-07,
same dates (powder); file: data/e1-activity-data.csv rows where location = The Frigate Bird

Sources: csrd/salacia-mapping.md §3, §6; csrd/e1-climate.md §Method an' evidence;
data/fleet.csv (NSG-07); lore/people.md (Captain-General)
```

**Why it passes.** Answered for one location only, by the officer who holds her; numbers
lifted from the hull's own rows; evidence named as the book an' page a clerk would scan;
internal register, bad news (the whale oil) said first an' plainly.
