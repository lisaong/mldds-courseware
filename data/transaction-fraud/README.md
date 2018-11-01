Data source: [Synthetic Financial Datasets For Fraud Detection](https://www.kaggle.com/ntnu-testimon/paysim1)

## Dataset: paysim_transactions_64k.csv

Subset of kaggle dataset of 64k entries, created by randomly sampling 1% of fraudulent and 0.1% of non-fradulant.

Attributes:
- step: Maps a unit of time in the real world. In this case 1 step is 1 hour of time.
- type: CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER
- amount: amount of the transaction in local currency
- nameOrig: customer who started the transaction
- oldbalanceOrg - initial balance before the transaction
- newbalanceOrig - customer's balance after the transaction.
- nameDest - recipient ID of the transaction.
- oldbalanceDest - initial recipient balance before the transaction.
- newbalanceDest - recipient's balance after the transaction.
- isFlaggedFraud - flags illegal attempts to transfer more than 200.000 in a single transaction.

Target variable to predict:
- isFraud - identifies a fraudulent transaction (1) and non fraudulent (0)