import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.rename_column.python.ExecutionHandler import ExecutionHandler

def test_rename_column():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112]})
    column = 'id_customer'
    new_name='new1'
    result = execution_handler.execute(Data, column, new_name)
    expected_result = pd.DataFrame({"new1": [0, 1], "Recency": [534, 112]})
    pd.testing.assert_frame_equal(result, expected_result)
