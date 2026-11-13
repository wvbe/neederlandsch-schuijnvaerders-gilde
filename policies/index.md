---
title: The Standin' Orders — register of the Gilde's written policies
status: draft
last-verified: 2026-11-13
canon-refs:
  - company.legal_name
  - company.chamber_count
  - reporting.base_year_label
  - reporting.base_year_key
  - reporting.reported_year_label
  - reporting.reported_year_key
  - policies_adopted_by
  - policies_milestones_set_by
  - policies_review
  - policies
  - governance.counterweight_officer
  - operations.technology_rule
---

# The Standin' Orders — register of the Gilde's written policies

This folder holds the written standin' orders (policies) of the
**Neederlandsch Schuijnvaerders Gilde N.V.** on the matters that weigh for the warmin' o' the
seas, the water, the livin' coasts, the use of what we buy, and on our dealings with the
hands, the folk o' the ports, them as take delivery, the houses that fit us out and the
authorities we petition. Each order gathers in one place what the Standards ask of a policy,
its actions, its targets and its metrics (ESRS 2 MDR-P, MDR-A, MDR-T and MDR-M). The topic
files under `csrd/` keep the facts of the reportin' year and point here for the course ahead.

The orders were adopted in writing by the **Kermis Council, October 2026**. They gather the
standin' orders already in force and the 2030 marks set by the
**Raad van Kapiteins, Kermis of 2025**, which also costed the year-by-year path toward them.
The written orders add a mark for 2050 to every target.

## The register

| Policy | Name | Standard term | ESRS | Accountable office | File |
| --- | --- | --- | --- | --- | --- |
| POL-E1 | The Vow of the Old Ways | Climate policy | E1-2, E1-3, E1-4 | Quartermaster-General | [e1-climate.md](e1-climate.md) |
| POL-E2 | The Clean Wake Order | Pollution policy | E2-1, E2-2, E2-3 | Quartermaster-General | [e2-pollution.md](e2-pollution.md) |
| POL-E3 | The Water Cask Order | Water and marine resources policy | E3-1, E3-2, E3-3 | Quartermaster-General | [e3-water-marine.md](e3-water-marine.md) |
| POL-E4 | The Living Coasts Order | Biodiversity and ecosystems policy | E4-2, E4-3, E4-4 | Quartermaster-General | [e4-biodiversity.md](e4-biodiversity.md) |
| POL-E5 | The Make-Do Order | Resource use and circular economy policy | E5-1, E5-2, E5-3 | Quartermaster-General | [e5-resources.md](e5-resources.md) |
| POL-S1 | The Articles and the Parley | Labour relations and social dialogue policy | S1-1, S1-2, S1-3, S1-4, S1-5, S1-8 | Quartermaster-General | [s1-labour-relations.md](s1-labour-relations.md) |
| POL-S2 | The Fitting-Out Order | Value-chain workers policy | S2-1 to S2-5 | Quartermaster-General | [s2-value-chain-workers.md](s2-value-chain-workers.md) |
| POL-S3 | The Good Neighbour Order | Affected communities policy | S3-1 to S3-5 | Captain-General | [s3-port-communities.md](s3-port-communities.md) |
| POL-S4 | The Honest Manifest Order | Consumers and end-users policy | S4-1 to S4-5 | Captain-General | [s4-consignees-clients.md](s4-consignees-clients.md) |
| POL-G1-2 | The Thirty Days Order | Supplier relations and payment practices policy | G1-2, G1-6 | Advocaat-Boekhouder | [g1-supplier-relations.md](g1-supplier-relations.md) |
| POL-G1-5 | The Open Petition Order | Political engagement policy | G1-5 | Captain-General | [g1-political-engagement.md](g1-political-engagement.md) |

The register is held in canon under `policies`, with the office that carries out each
order day to day.

## Which order answers which matter

Every matter that weighs in [the IRO register](../data/iros.csv) is answered by a written order
here, or by a standin' order that stays in its topic file. None is left without one.

| IRO | Matter (ESRS sub-topic) | Answered by |
| --- | --- | --- |
| IRO-01 to IRO-04 | Climate change mitigation and adaptation | [POL-E1](e1-climate.md) |
| IRO-05 to IRO-07 | Pollution of air and water | [POL-E2](e2-pollution.md) |
| IRO-08, IRO-10 | Water withdrawals | [POL-E3](e3-water-marine.md), which also holds the refusals on marine resources (IRO-09, not material) |
| IRO-11 to IRO-14 | Direct impact drivers of biodiversity loss; state of species | [POL-E4](e4-biodiversity.md) |
| IRO-15, IRO-16 | Resource inflows and outflows; waste | [POL-E5](e5-resources.md) |
| IRO-17 | Health and safety | The standin' orders in [S1-1](../csrd/s1-workforce.md), with their marks in S1-5 |
| IRO-18 | Adequate wages | The standin' orders in [S1-1](../csrd/s1-workforce.md), with their marks in S1-5 |
| IRO-20 | Social dialogue | [POL-S1](s1-labour-relations.md) |
| IRO-21 to IRO-23 | Working conditions and other work-related rights in the value chain | [POL-S2](s2-value-chain-workers.md) |
| IRO-24, IRO-25 | Communities' economic, social and cultural rights | [POL-S3](s3-port-communities.md) |
| IRO-26 | Information-related impacts for consumers and end-users | [POL-S4](s4-consignees-clients.md) |
| IRO-28 | Corporate culture | The articles and the commissie due diligence in [G1-1](../csrd/g1-conduct.md) |
| IRO-29 | Corruption and bribery | The standin' orders in [G1-3](../csrd/g1-conduct.md) |
| IRO-30 | Management of relationships with suppliers (the commission bond) | The commissie due diligence in [G1-1](../csrd/g1-conduct.md); payment practices in [POL-G1-2](g1-supplier-relations.md) |
| — | Political engagement (no material IRO; held as good conduct) | [POL-G1-5](g1-political-engagement.md) |

IRO-19 (forced labour) and IRO-27 (personal safety of consumers) fell below the line; the
Sainte-Marie clause and the refusals in [POL-S2](s2-value-chain-workers.md) and
[POL-S4](s4-consignees-clients.md) still bind.

## How a mark is set

1. **Years are Kermis years**, 1 October to 30 September. The year we measure from (base
   year) is FY2024, period key `102023-092024`. The reported year is FY2025, period key
   `102024-092025`.
2. **Every target carries five milestones and a long mark**: FY2026, FY2027, FY2028, FY2029
   and FY2030, and FY2050. The milestones are marks, not outcomes. FY2026 closed on
   2026-09-30. Its outcome is stated only once the Advocaat-Boekhouder has closed the
   ledgers for it; until then it is `[UNCHARTED]`. A target first set by the written orders
   in October 2026 carries no FY2026 milestone, for that year had closed before the mark was
   set; its first milestone is FY2027.
3. **The 2030 marks already set do not move.** The FY2030 milestone of every target equals
   the 2030 mark held in canon. A change is proposed to the Quartermaster-General with its
   reason, and stands only once it is in canon.
4. **Gross, never bought.** No mark is met by offsets, credits or anything bought in place
   of the work. No action and no 2050 mark may break the articles' rule on gear:
   "Nothing aboard or ashore that was not in use on a Dutch ship in the 1600s".
5. **All chambers.** From FY2026 every order covers all 6 chambers, Vava'u included. Where
   Vava'u has no measured value, its baseline is set in its first full year and the cell
   reads `[UNCHARTED]` until then. No value is supplied by estimate.
6. **Where the numbers live.** The year-by-year milestones are held in
   [the target register](../data/targets.csv), described in
   [its schema](../data/targets.schema.md). The 2030 and 2050 marks are held in canon beside
   the metric's FY2025 value. A policy file quotes both and adds nothing of its own.
7. **Review.** The orders are reviewed at
   every Kermis Council; marks reset no later than the Kermis of 2030. A missed milestone is reported first and plainly, with what will be done
   about it, and the mark is not lowered to meet the result.

## The shape of every order

Every file in this folder has the same sections, in this order, in the Council's voice
(formal register):

| Section | What it holds | ESRS |
| --- | --- | --- |
| Purpose | What the order is for, and the matters that weigh it answers, by IRO number from `data/iros.csv` | MDR-P 65(a) |
| Scope | Activities, hulls and chambers covered, where in the value chain, and any exclusion with its reason | MDR-P 65(b) |
| Accountability | The highest office answerable for the order, and who carries it out day to day | MDR-P 65(c) |
| Commitments | The standin' orders themselves, quoted as the articles or the Raad wrote them | MDR-P 65(a) |
| Standards and shipmates | Any outside standard the order follows, and whose interests were heard in setting it | MDR-P 65(d), 65(e) |
| How it is made known | How hands, suppliers and the folk o' the ports learn of it | MDR-P 65(f) |
| Actions FY2026 to FY2030 | Each action: what, where, when, the resources it takes, and the result it should bring | MDR-A 68 |
| Targets | One table: metric, unit, kind (absolute or relative), base FY2024, FY2025, FY2026 to FY2030, FY2050, scope | MDR-T 80 |
| Metrics | For each metric: definition, how it is counted, the tally it comes from, and its canon key | MDR-M 77 |
| Monitoring and review | Who reads the measures, how often, and what happens when a milestone is missed | MDR-T 80(j) |
| Related | Links to the topic file, the register and canon | — |

The Vow of the Old Ways (POL-E1) is the worked example of this shape.

## Who keeps the orders

The Quartermaster-General, as keeper of the common chest and the crews' counterweight, keeps
this register, reads every milestone against the ledgers at the Kermis Council, and decides
what enters canon. An order is changed only by the body that adopted it.

## Related

- [The target register](../data/targets.csv) and [its schema](../data/targets.schema.md)
- [Canon](../canon/facts.yaml), key `policies`
- [The double materiality assessment](../csrd/double-materiality.md) and [the IRO register](../data/iros.csv)
- [Salacia mapping](../csrd/salacia-mapping.md)
- [Voice and language](../brand/voice-and-language.md)
