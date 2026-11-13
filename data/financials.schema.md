# Financial statements register — schema

One row per line of the Gilde's consolidated financial statements and the notes that carry
an amount. This file is the machine layer of the annual reports under `../financial-reports/`;
the headline figures (turnover, operating result, net result, group equity, total assets,
cash, dividend) are also held in canon under `financials`, and canon wins if they disagree.

Years are Kermis years (1 October to 30 September), named for the calendar year in which they
end. For `balance_sheet` rows and the `notes` rows that state a position (cost, accumulated
depreciation, lease commitments), a year's cell is the position at 30 September of that year.
For `income_statement`, `cash_flow` and the other `notes` rows it is the amount for the year.
The `fy2021` column holds only the closing balance sheet of FY2021, the opening position of
the earliest comparative year shown (FY2022, in the FY2023 report). A cell is empty where no
value exists.

All amounts are in EUR thousand. Costs and cash outflows in the `cash_flow` statement are
negative; costs in the `income_statement` are positive and are deducted by the reader,
except `financial_expense` and `corporate_income_tax`, which carry their sign.

| Column | Description |
| --- | --- |
| statement | `income_statement`, `balance_sheet`, `cash_flow` or `notes` |
| line_key | Stable identifier of the line, lower case with underscores |
| line_label | The line as the annual report prints it, in plain English |
| unit | Always `EUR thousand` |
| fy2021 | Closing balance at 2021-09-30; balance-sheet and position rows only |
| fy2022 | FY2022, Kermis year 2021-10-01 to 2022-09-30 |
| fy2023 | FY2023, Kermis year 2022-10-01 to 2023-09-30 |
| fy2024 | FY2024, Kermis year 2023-10-01 to 2024-09-30; the base year of the sustainability statement |
| fy2025 | FY2025, Kermis year 2024-10-01 to 2025-09-30; the reported year |

```columns
statement
line_key
line_label
unit
fy2021
fy2022
fy2023
fy2024
fy2025
```

## How the statements tie

- `net_turnover` is the sum of the three `revenue_*` lines; FY2024 and FY2025 equal canon
  `scale.turnover_eur_base_year` and `scale.turnover_eur_reported_year`.
- `total_assets` equals `total_equity_and_liabilities` in every year.
- `group_equity` at the end of a year equals the opening equity plus `net_result` less the
  `dividend_paid` note of that year; dividends are paid in the year after the result is earned.
- `cf_net_change` equals the change in `cash` between two year ends.
- `trade_payables` is set so that trade payables over purchases (voyage, materials and other
  operating costs) times 365 approximates canon `g1.average_days_to_pay_fy2025` and
  `g1.average_days_to_pay_fy2024`.
