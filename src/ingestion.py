import pandas as pd

def load_transactions(file_path):
    transactions = pd.read_csv(file_path)

    return transactions