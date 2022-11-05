import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.duplicate_columns.python.ExecutionHandler import ExecutionHandler

def test_duplicate_columns():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112]})
    columns = ['id_customer', 'Recency']
    result = execution_handler.execute(Data,columns)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112],
                                    "id_customer_duplicate": [0, 1], "Recency_duplicate": [534, 112]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
