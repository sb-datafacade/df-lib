import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.concatenate_columns.python.ExecutionHandler import ExecutionHandler

def test_concatenate_columns():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": [10.25, 1.35], "col2": [10.25, 1.35]})
    columns = ['col1', 'col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35], "col2": [10.25, 1.35],
                                    'new_concatenated_col': ['10.25,10.25', '1.35,1.35']})
    pd.testing.assert_frame_equal(result, expected_result)
