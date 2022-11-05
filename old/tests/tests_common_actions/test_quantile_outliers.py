import numpy as np
import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.quantile_numeric_outliers.python.ExecutionHandler import ExecutionHandler


def test_quantile_outliers():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 500, -100]})
    column = 'col1'
    lower_quantile = 5
    upper_quantile = 80
    fix_method = 'clip'
    result = execution_handler.execute(Data, column, lower_quantile, upper_quantile, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 108.2, -79.73]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 500, -100]})
    column = 'col1'
    lower_quantile = 5
    upper_quantile = 80
    fix_method = 'remove'
    result = execution_handler.execute(Data, column, lower_quantile, upper_quantile, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 500, -100]})
    column = 'col1'
    lower_quantile = 5
    upper_quantile = 80
    fix_method = 'invalidate'
    result = execution_handler.execute(Data, column, lower_quantile, upper_quantile, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, np.nan, np.nan]})

    pd.testing.assert_frame_equal(result, expected_result)