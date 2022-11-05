import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.boolean_imputation.python.ExecutionHandler import ExecutionHandler


def test_boolean_impute():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': [True, False, False, False, True, np.nan, False, True],
                         'col2': [True, True, True, False, False, np.nan, True, False]})
    columns = ['col1', 'col2']
    imputation_method = 'Remove'
    result = execution_handler.execute(Data, columns, imputation_method).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col1': [True, False, False, False, True, False, True],
                                    'col2': [True, True, True, False, False, True, False]})

    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case2
    """
    Data = pd.DataFrame({'col1': [True, False, False, False, True, np.nan, False, True],
                         'col2': [True, True, True, False, False, np.nan, True, False]})
    columns = ['col1', 'col2']
    imputation_method = 'Replace'
    result = execution_handler.execute(Data, columns, imputation_method)
    expected_result = pd.DataFrame({'col1': [True, False, False, False, True, False, False, True],
                                    'col2': [True, True, True, False, False, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
