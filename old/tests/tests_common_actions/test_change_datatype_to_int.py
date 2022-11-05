import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.change_data_type_to_int.python.ExecutionHandler import ExecutionHandler



def test_change_datatype_to_int():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id": [0.0, 1.0], "int_id": ['0', '1']})
    columns = ['id', 'int_id']
    expected_result = pd.DataFrame({"id": [0, 1], "int_id": [0, 1]})
    result = execution_handler.execute(Data, columns)
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
