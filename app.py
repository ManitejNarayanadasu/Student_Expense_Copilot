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

print("Raw data:")
print(transactions)

# Validate required columns
validate_columns(transactions)

# Clean the data
transactions = clean_transactions(transactions)

# Validate cleaned values
validate_values(transactions)

print("\nCleaned data:")
print(transactions)

print("\nData types:")
print(transactions.dtypes)

#Catergorise data
categorised_results = transactions["Description"].apply(categorise_transaction)

transactions["Category"] = categorised_results.apply(lambda result: result[0])
transactions["Subcategory"] = categorised_results.apply(lambda result: result[1])

print(transactions[["Description", "Category", "Subcategory"]])
                                 