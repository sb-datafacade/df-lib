import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.flatten_vectors.python.ExecutionHandler import ExecutionHandler


def test_flatten_vectors():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col1': [np.array([["A", 'b'], ["A", 'b']]), np.array([["A", 'b'], ["A", 'b']])],
                         'col2': [np.array([["A", 'b'], ["A", 'b']]), np.array([["A", 'b'], ["A", 'b']])]})
    columns = ['col1', 'col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({'col1': [np.array([["A", 'b'], ["A", 'b']]), np.array([["A", 'b'], ["A", 'b']])],
                                    'col2': [np.array([["A", 'b'], ["A", 'b']]), np.array([["A", 'b'], ["A", 'b']])],
                                    'flattened_col1': [np.array(['A', 'A', 'b', 'b']), np.array(['A', 'A', 'b', 'b'])],
                                    'flattened_col2': [np.array(['A', 'A', 'b', 'b']), np.array(['A', 'A', 'b', 'b'])]})

    pd.testing.assert_frame_equal(result, expected_result)

