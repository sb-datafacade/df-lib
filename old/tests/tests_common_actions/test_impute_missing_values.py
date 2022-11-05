import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.impute_missing_values_to_new_column.python.ExecutionHandler import ExecutionHandler


def test_impute_missing_values():
    execution_handler = ExecutionHandler()

    """
    -case1
    """
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan]})
    columns = ['col1', 'col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                                    'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan],
                                    'new_col1': [1.00, 2.25, 1, 2, 2, 0, 4, 4],
                                    'new_col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan]})

    pd.testing.assert_frame_equal(result, expected_result)
    """
    -case2
    """
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan]})
    columns = ['col1', 'col2']
    algorithm = 'mode'
    result = execution_handler.execute(Data, columns, algorithm)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                                    'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan],
                                    'new_col1': [1.00, 2.25, 1, 2, 2, 1, 4, 4],
                                    'new_col2': ['A', 'A', 'A', 'E', 'A', 'A', 'A', 'A']})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({'col1': [1.00, 5.0, 1, 2, 3, np.nan, 5, 4]})
    columns = ['col1']
    algorithm = 'mean'
    result = execution_handler.execute(Data, columns, algorithm)
    expected_result = pd.DataFrame({'col1': [1.00, 5.0, 1, 2, 3, np.nan, 5, 4],
                                    'new_col1': [1.00, 5.0, 1, 2, 3, 3, 5, 4]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case4
    """
    Data = pd.DataFrame({'col1': [1.00, 5.0, 1, 2, 3, np.nan, 5, 4]})
    columns = ['col1']
    algorithm = 'median'
    result = execution_handler.execute(Data, columns, algorithm)
    expected_result = pd.DataFrame({'col1': [1.00, 5.0, 1, 2, 3, np.nan, 5, 4],
                                    'new_col1': [1.00, 5.0, 1, 2, 3, 3, 5, 4]})
    pd.testing.assert_frame_equal(result, expected_result)




