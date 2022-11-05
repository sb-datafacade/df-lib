import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_right_strip.python.ExecutionHandler import ExecutionHandler




def test_string_right_strip():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['test**', "/*/test train/1/"],
                         "col2": ['t//', "trail111"]})
    columns = ['col1','col2']
    charecters = '*/1'
    result = execution_handler.execute(Data, columns, charecters)
    expected_result = pd.DataFrame({"col1": ['test', "/*/test train"],
                                    'col2': ['t', 'trail']})

    pd.testing.assert_frame_equal(result, expected_result)