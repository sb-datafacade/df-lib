import pandas as pd
import random
from applications.DataFacadeOOB.code.ActionDefinition.write_table_to_googlesheets.python.ExecutionHandler import \
    ExecutionHandler


def test_write_to_gsheet():
    execution_handler = ExecutionHandler()
    df = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 534], "T": [534, 534], "Frequency": [1, 2],
                       "Monetary.min": [100, 100], "Monetary.avg": [100, 100], "Monetary.max": [100, 100],
                       "Monetary": [100.0, 100.0]})
    spreadsheet_id = "1HfyLbFg4XQkK1K64XDkxcKCKNpwTBmyyK0vsGQ-x2lw"
    sheet_name = 'Sheet'+str(random.getrandbits(16))
    result = execution_handler.execute(df, spreadsheet_id, sheet_name)
