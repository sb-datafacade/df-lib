import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.transform_to_capitalize.python.ExecutionHandler import ExecutionHandler


def test_transform_capitalize():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['test', "train"],
                         "col2": ['t', "train"]})
    columns = ['col1','col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['Test', "Train"],
                                    'col2': ['T', 'Train']})

    pd.testing.assert_frame_equal(result, expected_result)