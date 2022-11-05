import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.convert_columns_to_date_time_format.python.ExecutionHandler import ExecutionHandler

def test_convert_date_col():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id": [0, 1], "date": [20221012, 20021214], "int_id": [0, 1], "value": [0, 1]})
    date_columns = ['date']
    result = execution_handler.execute(Data, date_columns)
    expected_result = pd.DataFrame({"id": [0, 1], "date": pd.to_datetime(['2022/10/12', '2002/12/14']), "int_id": [0, 1], "value": [0, 1]})
    pd.testing.assert_frame_equal(result,expected_result)
