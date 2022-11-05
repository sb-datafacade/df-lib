import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.drop_column_with_null.python.ExecutionHandler import ExecutionHandler


def test_drop_column_with_null():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col1': [np.nan, np.nan, np.nan], 'col2':[1000.0, 10.25, 100.55]})
    result = execution_handler.execute(Data)
    expected_result = pd.DataFrame({'col2': [1000.0, 10.25, 100.55]})
    pd.testing.assert_frame_equal(result, expected_result)
