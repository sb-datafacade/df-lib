import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_remove_symbols.python.ExecutionHandler import ExecutionHandler





def test_string_remove_symbols():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['***test', "*/*test train/1/"],
                         "col2": ['////t', "111trail"]})
    columns = ['col1','col2']
    symbols = '/*1'
    result = execution_handler.execute(Data, columns, symbols)
    expected_result = pd.DataFrame({"col1": ['test', "test train"],
                                    'col2': ['t', 'trail']})

    pd.testing.assert_frame_equal(result, expected_result)