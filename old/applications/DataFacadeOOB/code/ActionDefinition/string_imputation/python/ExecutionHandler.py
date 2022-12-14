"""
Inputs:
    - data: Source data in the form of dataframe
    - columns: List of columns for which string imputation need to be done
    - value_percentage: Threshold value to determine whether the string column is categorical type (e.g. Gender,Occupation)
                        or unique identifier (e.g. Name,Email ID) (default 50%)
Output:
    - Data in the form of dataframe with imputed columns
"""
import pandas as pd
import numpy as np
from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, data: pd.DataFrame, columns: [str], value_percentage=50):

        df_columns = data.columns.tolist()
        try:
            for col in columns:
                if col not in df_columns:
                    continue

                if len(data[col]) and len(data[col].unique()) / len(data[col]) > (value_percentage / 100):

                    remove_row = data[col].isna()
                    remove_row = np.where(remove_row)[0]
                    remove_row = remove_row.tolist()
                    if len(remove_row) > 0:
                        data.drop(remove_row, axis=0, inplace=True)

                else:
                    data[col].fillna(data[col].value_counts().index[0], inplace=True)

        except Exception as e:
            raise type(e)(e)

        return data
