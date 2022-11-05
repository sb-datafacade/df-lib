import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.missing_value_indicator_column.python.ExecutionHandler import ExecutionHandler


def test_missing_value_indicator():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                         'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan]})
    result = execution_handler.execute(Data)
    expected_result = pd.DataFrame({'col1': [1.00, 2.25, 1, 2, 2, np.nan, 4, 4],
                                    'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan],
                                    'Missing_Value_Indicator': [False, True, False, False, False, True, True, True]})

    pd.testing.assert_frame_equal(result, expected_result)