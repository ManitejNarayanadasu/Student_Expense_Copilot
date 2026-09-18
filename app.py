import pandas as pd
from src.ingestion import load_transactions
from src.cleaning import (
    validate_columns,
    clean_transactions,
    validate_values
)
from src.categorisation import categorise_transaction


# Load raw transactions
transactions = load_transactions(
    "data/sample_transactions.csv"
)

# Validate required columns
validate_columns(transactions)

# Clean the data
transactions = clean_transactions(transactions)

# Validate cleaned values
validate_values(transactions)

print("\nCleaned data:")
print(transactions)

#Catergorise data
categorised_results = transactions["Description"].apply(categorise_transaction)

transactions["Category"] = categorised_results.apply(lambda result: result[0])
transactions["Subcategory"] = categorised_results.apply(lambda result: result[1])

print(transactions[["Description", "Category", "Subcategory"]])

#Group recurring payments
##group by dates
dates = transactions.groupby("Description")["Date"].agg(list)

recurring_status = {}
for description, date_list in dates.items():
    if len(date_list) < 2:
        recurring_status[description] = False
    else:
        intervals = []
        for i, j in zip(date_list,date_list[1:]):
            difference = j - i
            intervals.append(difference.days)
        if all(25 <= interval <= 35 for interval in intervals):
            recurring_status[description] = True
        else:
            recurring_status[description] = False
transactions["Recurring"] = transactions["Description"].map(recurring_status)
print(transactions)
print(transactions[["Description", "Date", "Recurring"]])



