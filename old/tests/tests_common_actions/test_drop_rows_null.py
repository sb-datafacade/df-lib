import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.drop_rows_with_null.python.ExecutionHandler import ExecutionHandler


def test_drop_rows_null():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col1': ['A', np.nan, 'E', 'E', 'E', np.nan,'E', np.nan],
                         'col2': ['A', np.nan, 'A', 'E', 'A', np.nan, np.nan, np.nan]})
    null_percentage = 45
    result = execution_handler.execute(Data, null_percentage)
    expected_result = pd.DataFrame({'col1': ['A', 'E', 'E', 'E'],
                                    'col2': ['A', 'A', 'E', 'A']})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    Data = pd.DataFrame({'col1': ['A', np.nan, 'E', 'E', 'E', np.nan, 'E', np.nan],
                         'col2': ['A', np.nan, 'A', 'E', 'A', np.nan, np.nan, np.nan]})
    null_percentage = 100
    result = execution_handler.execute(Data, null_percentage)
    expected_result = pd.DataFrame({'col1': ['A', 'E', 'E', 'E', 'E'],
                                    'col2': ['A', 'A', 'E', 'A', np.nan]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
