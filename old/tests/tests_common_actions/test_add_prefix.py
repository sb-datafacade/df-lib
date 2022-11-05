import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_add_prefix.python.ExecutionHandler import ExecutionHandler


def test_add_prefix():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['test', "train"],
                         "col2": ['test', "train"]})
    columns = ['col1','col2']
    prefix=['split ']
    result = execution_handler.execute(Data, columns, prefix)
    expected_result = pd.DataFrame({"col1": ['split test', "split train"],
                                    'col2': ['split test', 'split train']})

    pd.testing.assert_frame_equal(result, expected_result)