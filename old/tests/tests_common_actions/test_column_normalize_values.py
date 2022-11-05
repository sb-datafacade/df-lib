import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.column_normalize_values.python.ExecutionHandler import ExecutionHandler

def test_column_normalize_values():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": [10.25, 1.35,2.55]})
    columns = ['col1']
    result = execution_handler.execute(Data,columns)
    expected_result= pd.DataFrame({"col1": [1.403257, -0.853789,-0.549468]})
    pd.testing.assert_frame_equal(result,expected_result)
