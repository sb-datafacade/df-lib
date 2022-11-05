import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_left_strip.python.ExecutionHandler import ExecutionHandler




def test_string_left_strip():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['***test', "/*/test train/1/"],
                         "col2": ['////t', "111trail"]})
    columns = ['col1','col2']
    charecters = '*/1'
    result = execution_handler.execute(Data, columns, charecters)
    expected_result = pd.DataFrame({"col1": ['test', "test train/1/"],
                                    'col2': ['t', 'trail']})

    pd.testing.assert_frame_equal(result, expected_result)