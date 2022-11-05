import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.min_max_numeric_outliers.python.ExecutionHandler import ExecutionHandler


def test_min_max_outliers():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 500, -100]})
    column = 'col1'
    lower_threshold = 0
    upper_threshold = 50
    fix_method = 'clip'
    result = execution_handler.execute(Data, column, lower_threshold, upper_threshold, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 50, 0]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 500, -100]})
    column = 'col1'
    lower_threshold = 0
    upper_threshold = 50
    fix_method = 'remove'
    result = execution_handler.execute(Data, column, lower_threshold, upper_threshold, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 500, -100]})
    column = 'col1'
    lower_threshold = 0
    upper_threshold = 50
    fix_method = 'invalidate'
    result = execution_handler.execute(Data, column, lower_threshold, upper_threshold, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, np.nan, np.nan]})

    pd.testing.assert_frame_equal(result, expected_result)