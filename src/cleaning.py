import pandas as pd


REQUIRED_COLUMNS = ["Date", "Description", "Amount"]


def validate_columns(transactions):
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in transactions.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return True

def clean_transactions(transactions):
    transactions = transactions.copy()

    # Remove extra spaces from column names
    transactions.columns = transactions.columns.str.strip()

    # Remove extra spaces from descriptions
    transactions["Description"] = (
        transactions["Description"]
        .astype("string")
        .str.strip()
    )

    # Convert dates into datetime objects
    transactions["Date"] = pd.to_datetime(
        transactions["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Convert amounts into numbers
    transactions["Amount"] = pd.to_numeric(
        transactions["Amount"],
        errors="coerce"
    )

    return transactions

def validate_values(transactions):
    invalid_dates = transactions["Date"].isna().sum()
    invalid_amounts = transactions["Amount"].isna().sum()
    missing_descriptions = transactions["Description"].isna().sum()

    if invalid_dates > 0:
        raise ValueError(
            f"Found {invalid_dates} invalid date(s)."
        )

    if invalid_amounts > 0:
        raise ValueError(
            f"Found {invalid_amounts} invalid amount(s)."
        )

    if missing_descriptions > 0:
        raise ValueError(
            f"Found {missing_descriptions} missing description(s)."
        )

    return True