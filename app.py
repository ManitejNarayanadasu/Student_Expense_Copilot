from src.ingestion import load_transactions
from src.cleaning import (
    validate_columns,
    clean_transactions,
    validate_values
)


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