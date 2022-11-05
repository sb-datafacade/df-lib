import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_values_encode.python.ExecutionHandler import \
    ExecutionHandler


def test_one_hot_encode():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col2': ['A', 'B', 'C', 'E']})
    columns = ['col2']
    drop_columns = True
    result = execution_handler.execute(Data, columns, drop_columns)
    expected_result = pd.DataFrame({'col2_A': [1.00, 0, 0, 0],
                                    'col2_B': [0, 1.00, 0, 0],
                                    'col2_C': [0, 0, 1.00, 0],
                                    'col2_E': [0, 0, 0, 1.00]})

    pd.testing.assert_frame_equal(result, expected_result)

    Data = pd.DataFrame({'col2': ['A', 'B', 'C', 'E', 'F', 'G']})
    columns = ['col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({'col2': ['A', 'B', 'C', 'E', 'F', 'G'],
                                    'col2_ordinal_encode': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]})

    pd.testing.assert_frame_equal(result, expected_result)
