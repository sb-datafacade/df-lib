import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.shuffle_row.python.ExecutionHandler import ExecutionHandler


def test_shuffle_row():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 4],
                         'col2': [8, 3, 9, 6]})
    result = execution_handler.execute(Data).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({"col1": [2.55, 10.25, 4.00, 1.35],
                                    'col2': [9, 8, 6, 3]})

    pd.testing.assert_frame_equal(result, expected_result)
