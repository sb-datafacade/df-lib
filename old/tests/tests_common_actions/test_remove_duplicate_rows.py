import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.remove_duplicate_rows.python.ExecutionHandler import ExecutionHandler

def test_remove_duplicate_rows():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1,1], "Recency": [534, 112,112]})
    result = execution_handler.execute(Data)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112]})
    pd.testing.assert_frame_equal(result, expected_result)
