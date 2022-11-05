import pandas as pd
import os


def load_data(file_name='salesforce_data_with_duplicates.csv'):
    current_path = os.path.dirname(__file__)
    data = pd.read_csv(current_path + f"/data/{file_name}")
    return data
