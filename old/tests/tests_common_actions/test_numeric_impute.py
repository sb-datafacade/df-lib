import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.numeric_impute.python.ExecutionHandler import ExecutionHandler


def test_numeric_impute():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': [1, 2, 1, 2, 2, np.nan, 4, 4]})
    columns = ['col1', 'col2']
    imputation_method = 'Remove'
    result = execution_handler.execute(Data, columns, imputation_method).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, 4, 4],
                                    'col2': [1, 2, 1, 2, 2, 4, 4]})

    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case2
    """
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': [1, 2, 1, 2, 2, np.nan, 4, 4]})
    columns = ['col1', 'col2']
    imputation_method = 'Mean'
    result = execution_handler.execute(Data, columns, imputation_method)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, 2.32, 4, 4],
                                    'col2': [1, 2, 1, 2, 2, 2.29, 4, 4]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': [1, 2, 1, 2, 2, np.nan, 4, 4]})
    columns = ['col1', 'col2']
    imputation_method = 'Median'
    result = execution_handler.execute(Data, columns, imputation_method)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, 2, 4, 4],
                                    'col2': [1, 2, 1, 2, 2, 2, 4, 4]})

    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case4
    """
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': [1, 2, 1, 2, 2, np.nan, 4, 4]})
    columns = ['col1', 'col2']
    imputation_method = 'Mode'
    result = execution_handler.execute(Data, columns, imputation_method)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, 1, 4, 4],
                                    'col2': [1, 2, 1, 2, 2, 2, 4, 4]})

    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
