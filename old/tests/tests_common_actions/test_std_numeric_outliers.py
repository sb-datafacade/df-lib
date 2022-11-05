import numpy as np
import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.standard_deviation_numeric_outliers.python.ExecutionHandler import ExecutionHandler


def test_std_numeric_outliers():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -20]})
    column = 'col1'
    number_of_sd = 1
    fix_method = 'clip'
    result = execution_handler.execute(Data, [column], number_of_sd, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 17.606189, -11.946189]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -20]})
    column = 'col1'
    number_of_sd = 1
    fix_method = 'remove'
    result = execution_handler.execute(Data, [column], number_of_sd, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 20, -20]})
    column = 'col1'
    number_of_sd = 1
    fix_method = 'invalidate'
    result = execution_handler.execute(Data, [column], number_of_sd, fix_method)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55, np.nan, np.nan]})


    pd.testing.assert_frame_equal(result, expected_result)