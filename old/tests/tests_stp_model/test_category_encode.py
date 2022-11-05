import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.categorical_column_encoding.python.ExecutionHandler import ExecutionHandler


def test_category_encode():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': ['A', 'B', 'C', 'E', 'F', 'G'],
                         'col2': ['A', 'B', 'C', 'E', 'E', 'A']})
    result = execution_handler.execute(Data)
    expected_result = pd.DataFrame({'col2_A': [1.00, 0, 0, 0, 0, 1.0],
                                    'col2_B': [0, 1.00, 0, 0, 0, 0],
                                    'col2_C': [0, 0, 1.00, 0, 0, 0],
                                    'col2_E': [0, 0, 0, 1.00, 1.00, 0],
                                    'col1_encode': [0.0, 1, 2, 3, 4, 5]})
    pd.testing.assert_frame_equal(result, expected_result)
    """
    -case2
    """
    Data = pd.DataFrame({'col1': ['A', 'B', 'C', 'E', 'F', 'G', 'Hi', 'Gi', 'Pi', 'Le', 'Ai', 'Bi']})
    result = execution_handler.execute(Data).round(2)
    expected_result = pd.DataFrame({'col1_0': [1.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.12, 0],
                                    'col1_1': [0.12, 0.00, 0, 0, 0, 0, 0.09, 0.09, 0.09, 0.0, 1.0, 0.09],
                                    })
    pd.testing.assert_frame_equal(result[['col1_0', 'col1_1']], expected_result)

