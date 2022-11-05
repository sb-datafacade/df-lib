import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.string_imputation.python.ExecutionHandler import ExecutionHandler


def test_string_imputation():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col1': ['A', np.nan, 'B', 'E', 'D', 'D', 'A', np.nan],
                         'col2': ['A', np.nan, 'A', 'E', 'A', 'A', np.nan, np.nan]})
    columns = ['col1', 'col2']
    value_percentage = 60
    result = execution_handler.execute(Data, columns, value_percentage).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col1': ['A', 'B', 'E', 'D', 'D', 'A'],
                                    'col2': ['A', 'A', 'E', 'A', 'A', 'A']})

    pd.testing.assert_frame_equal(result, expected_result)