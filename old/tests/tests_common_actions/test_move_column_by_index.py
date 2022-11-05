import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.move_column_by_index.python.ExecutionHandler import \
    ExecutionHandler


def test_move_column_by_index():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112],
                         "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    column = 'Monetary'
    index = 'start'
    result = execution_handler.execute(Data, column, index)
    expected_result = pd.DataFrame({"Monetary": [100.0, 200.0], "id_customer": [0, 1], "Recency": [534, 112],
                                    "T": [534, 112], "Frequency": [1, 1]})
    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112],
                         "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    column = 'Frequency'
    index = 'end'
    result = execution_handler.execute(Data, column, index)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112],
                                    "T": [534, 112], "Monetary": [100.0, 200.0], "Frequency": [1, 1]})
    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112],
                         "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    column = 'T'
    index = '2'
    result = execution_handler.execute(Data, column, index)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "T": [534, 112], "Recency": [534, 112],
                                    "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    pd.testing.assert_frame_equal(result, expected_result)
