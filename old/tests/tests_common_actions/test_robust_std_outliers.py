import numpy as np
import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.robust_standard_deviation_numeric_outliers.python.ExecutionHandler import ExecutionHandler


def test_robust_std_outliers():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -25]})
    column = 'col1'
    lower_quantile = 25
    upper_quantile = 75
    number_of_sd = 2
    fix_method = 'clip'
    result = execution_handler.execute(Data, [column], lower_quantile, upper_quantile, number_of_sd, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -16.45]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -25]})
    column = 'col1'
    lower_quantile = 25
    upper_quantile = 75
    number_of_sd = 2
    fix_method = 'remove'
    result = execution_handler.execute(Data, [column], lower_quantile, upper_quantile, number_of_sd, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -25]})
    column = 'col1'
    lower_quantile = 25
    upper_quantile = 75
    number_of_sd = 2
    fix_method = 'invalidate'
    result = execution_handler.execute(Data, [column], lower_quantile, upper_quantile, number_of_sd, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, np.nan]})

    pd.testing.assert_frame_equal(result, expected_result)