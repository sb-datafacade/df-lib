import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_right_pad.python.ExecutionHandler import ExecutionHandler



def test_string_right_pad():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['test', "traintest train"],
                         "col2": ['t', "trail"]})
    columns = ['col1','col2']
    width = 10
    char = 'X'
    result = execution_handler.execute(Data, columns, width, char)
    expected_result = pd.DataFrame({"col1": ['testXXXXXX', "traintest "],
                                    'col2': ['tXXXXXXXXX', 'trailXXXXX']})

    pd.testing.assert_frame_equal(result, expected_result)
