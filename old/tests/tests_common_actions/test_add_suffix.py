import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_add_suffix.python.ExecutionHandler import ExecutionHandler


def test_add_suffix():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['test', "train"],
                         "col2": ['test', "train"]})
    columns = ['col1','col2']
    prefix=[' data']
    result = execution_handler.execute(Data, columns, prefix)
    expected_result = pd.DataFrame({"col1": ['test data', "train data"],
                                    'col2': ['test data', 'train data']})

    pd.testing.assert_frame_equal(result, expected_result)