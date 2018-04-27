1.动量和反转因子

| 因子名称    | 含义                     | 公式                         |
| ----------- | ------------------------ | ---------------------------- |
| RTN1D       | Total return, 1D         | PRICE(t)/PRICE(t-1)-1        |
| RTN5D       | Total return, 5D (1W)    | PRICE(t)/PRICE(t-5)-1        |
| RTN20D      | Total return, 20D (1M)   | PRICE(t)/PRICE(t-20)-1       |
| RTN3M       | Total return, 60D (3M)   | PRICE(t)/PRICE(t-60)-1       |
| RTN6M       | Total return, 120D (3M)  | PRICE(t)/PRICE(t-120)-1      |
| P_1averageG | Price-to-1 month average | PRICE(t)/average(PRICE, 20)  |
| P_3averageG | Price-to-3 month average | PRICE(t)/average(PRICE, 60)  |
| P_6averageG | Price-to-6 month average | PRICE(t)/average(PRICE, 120) |



2.技术因子

| 因子名称 | 含义                         | 公式                                              |
| -------- | ---------------------------- | ------------------------------------------------- |
| TO1D     | Turnover ratio, 1D           | turnover_d                                        |
| TO5D     | Turnover ratio, 1W           | sum(turnover_d, 5)                                |
| TO1M     | Turnover ratio, 1M           | sum(turnover_d, 20)                               |
| TO3M     | Turnover ratio, 3M           | sum(turnover_d, 60)                               |
| TO6M     | Turnover ratio, 6M           | sum(turnover_d, 120)                              |
| RSI1W    | Relative strength index, 5D  | max{PRICE - PRICE(t-1), 0},                       |
| RSI1M    | Relative strength index, 20D | max{PRICE(t-1) - PRICE, 0},                       |
| RSI3M    | Relative strength index, 60D | average(U, 5/20/60/120)/average(D,  5/20/60/120), |
| Beta     | 240 days HS300 beta          | regress(RTN1D, HS300, 240)                        |



3.价值和成长因子

| 因子名称  | 含义                         |
| --------- | ---------------------------- |
| BP        | book to price                |
| CFP       | Operate cashflow to price    |
| DP        | Dividend yield, trailing 12M |
| EP        | Earnings to price            |
| YoYP      | YoY Growth Rate - Profit (%) |
| YoYEquity | YoY Growth Rate - equity     |
| YoYAsset  | YoY Growth Rate - asset      |



4.基本面因子

| 因子名称   | 含义                             |
| ---------- | -------------------------------- |
| MV_total   | Total market value               |
| MV_float   | Float market value               |
| ARTurnDays | Account Receivable Turnover Days |
| AssetTurn  | asset turnover                   |