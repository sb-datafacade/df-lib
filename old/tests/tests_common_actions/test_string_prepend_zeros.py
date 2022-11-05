import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_prepend_zeros.python.ExecutionHandler import ExecutionHandler



def test_string_prepend_zeros():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['test', "traintest train"],
                         "col2": ['t', "trail"]})
    columns = ['col1','col2']
    width = 10
    result = execution_handler.execute(Data, columns, width)
    expected_result = pd.DataFrame({"col1": ['000000test', "test train"],
                                    'col2': ['000000000t', '00000trail']})

    pd.testing.assert_frame_equal(result, expected_result)
