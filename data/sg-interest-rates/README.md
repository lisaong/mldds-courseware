Data source: https://secure.mas.gov.sg/msb/InterestRatesOfBanksAndFinanceCompanies.aspx


## Dataset: prime_lending_rates_1983-2018_6mth_window.csv

Attributes:

- current_date: the current year and month (for reference)
- t-5: interest rate at (current_date - 5 months), in % p.a.
- t-4: interest rate at (current_date - 4 months), in % p.a.
- t-3: interest rate at (current_date - 3 months), in % p.a.
- t-2: interest rate at (current_date - 2 months), in % p.a.
- t-1: interest rate at (current_date - 1 month), in % p.a.

Target variable to predict:
- current_rate: interest rate at current_date, in % p.a.