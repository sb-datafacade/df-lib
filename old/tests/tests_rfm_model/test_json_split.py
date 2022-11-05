import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.json_column_split.python.ExecutionHandler import ExecutionHandler

def test_json_split():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['{2:100,3:100}', '{2:100,3:100}']})
    date_columns = ['col1']
    result = execution_handler.execute(Data,date_columns)
    expected_result= pd.DataFrame({"col1_2": [100, 100], "col1_3":[100,100]})
    pd.testing.assert_frame_equal(result,expected_result)
