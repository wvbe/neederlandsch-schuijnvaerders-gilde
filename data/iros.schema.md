# IRO register — schema

One row per impact, risk or opportunity identified in the double materiality assessment
(the reckonin' o' what matters) for the reporting year `102024-092025`. The method, the
bounded criteria, the thresholds and the outcome per ESRS topic live in
`../csrd/double-materiality.md`; this file is the machine layer of that narrative and the
register the Salacia platform's DMA module is loaded from. Scores are integers 1 to 5 and
are empty where the criterion does not apply: risks and opportunities carry no impact
scores, and impacts carry financial scores only where they also bear a financial effect.
Fields containing commas are quoted.

| Column | Description |
| --- | --- |
| iro_id | Identifier of the row, `IRO-01` to `IRO-30`, stable across reporting years |
| topic_code | Short code of the Gilde's materiality topic, aligned one to one with the ESRS topic: `E1` to `E5`, `S1` to `S4`, `G1` |
| topic_name_gilde | The Gilde's own wording for the topic, as the topic register in `../csrd/double-materiality.md` spells it |
| esrs_topic | Topic of the European Sustainability Reporting Standards the row is mapped to, code and standard name |
| esrs_subtopic | Sub-topic of that standard, as ESRS 1 Appendix A names it |
| iro_type | One of `negative impact`, `positive impact`, `risk`, `opportunity` |
| description | One line naming the impact, risk or opportunity, in the Gilde's formal register |
| value_chain_position | Where it arises: `upstream`, `own operations` or `downstream` |
| time_horizon | `short` (1 year), `medium` (5 years) or `long` (to 2050), as declared under ESRS 2 BP-2 |
| actual_or_potential | `actual` or `potential` for an impact; `n/a` for a risk or an opportunity |
| scale | Gravity of the impact, 1 to 5; empty for a risk or an opportunity |
| scope | How widespread the impact is, 1 to 5; empty for a risk or an opportunity |
| irremediability | How hard the impact is to put right, 1 to 5; empty for a positive impact, a risk or an opportunity |
| likelihood | Likelihood of the impact, 1 to 5, and always 5 for an actual impact; empty for a risk or an opportunity |
| impact_severity | Mean of scale, scope and irremediability to one decimal; for a positive impact, the mean of scale and scope only |
| impact_score | `impact_severity` times `likelihood`, to one decimal, on a scale of 25 |
| financial_magnitude | Size of the financial effect on the Gilde's purse, 1 to 5; empty where the row bears none |
| financial_likelihood | Likelihood of that financial effect, 1 to 5; empty where the row bears none |
| financial_score | `financial_magnitude` times `financial_likelihood`, on a scale of 25 |
| impact_material | `true` where `impact_score` is 9 or more, or the impact is actual and its severity is 4 or more; `false` otherwise |
| financial_material | `true` where `financial_score` is 9 or more; `false` otherwise |
| material | `true` where `impact_material` or `financial_material` is `true`; this column carries the row into the reckonin' |
| source_file | File under `../csrd/` where the row is answered: `e1-climate.md`, `e2-e5-environment.md`, `s1-workforce.md`, `s2-s4-value-chain-communities.md` or `g1-conduct.md` |

```columns
iro_id
topic_code
topic_name_gilde
esrs_topic
esrs_subtopic
iro_type
description
value_chain_position
time_horizon
actual_or_potential
scale
scope
irremediability
likelihood
impact_severity
impact_score
financial_magnitude
financial_likelihood
financial_score
impact_material
financial_material
material
source_file
```
