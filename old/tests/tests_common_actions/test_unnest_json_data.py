import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.unnest_json_data.python.ExecutionHandler import ExecutionHandler


def test_unnest_json_data():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['{2:100,3:100}', '{2:100,3:100}']})
    date_columns = ['col1']
    result = execution_handler.execute(Data,date_columns)
    expected_result= pd.DataFrame({"col1_2": [100, 100], "col1_3":[100,100]})
    pd.testing.assert_frame_equal(result,expected_result)