import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.drop_columns.python.ExecutionHandler import ExecutionHandler

def test_drop_columns():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112], "Frequency": [1, 1],
                        "Monetary.min": [100,200], "Monetary.avg": [100, 200],
                         "Monetary.max": [100,200], "Monetary": [100.0, 200.0]})
    columns = ['id_customer', 'Recency', 'T', 'Frequency', 'Monetary']
    result = execution_handler.execute(Data,columns)
    expected_result = pd.DataFrame({"Monetary.min": [100, 200], "Monetary.avg": [100.0, 200.0],
                                    "Monetary.max": [100, 200]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
