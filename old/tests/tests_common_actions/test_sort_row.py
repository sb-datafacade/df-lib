import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.sort_row.python.ExecutionHandler import ExecutionHandler


def test_sort_row():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 4],
                         'col2': [8, 3, 9, 6]})
    column = 'col1'
    ascending = True
    result = execution_handler.execute(Data, column, ascending)
    expected_result = pd.DataFrame({"col1": [1.35, 2.55, 4.00, 10.25],
                                    'col2': [3, 9, 6, 8]})

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 4],
                         'col2': [8, 3, 9, 6]})
    column = 'col1'
    ascending = False
    result = execution_handler.execute(Data, column, ascending)
    expected_result = pd.DataFrame({"col1": [10.25, 4.00, 2.55, 1.35],
                                    'col2': [8, 6, 9, 3]})

    pd.testing.assert_frame_equal(result, expected_result)
