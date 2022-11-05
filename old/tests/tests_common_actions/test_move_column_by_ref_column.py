import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.move_column_by_reference_column.python.ExecutionHandler import \
    ExecutionHandler


def test_move_column_by_ref_column():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112],
                         "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    column = 'Monetary'
    reference_column = 'id_customer'
    position = 'Before'
    result = execution_handler.execute(Data, column, reference_column, position)
    expected_result = pd.DataFrame({"Monetary": [100.0, 200.0], "id_customer": [0, 1], "Recency": [534, 112],
                                    "T": [534, 112], "Frequency": [1, 1]})
    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """

    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112],
                         "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    column = 'Monetary'
    reference_column = 'id_customer'
    position = 'After'
    result = execution_handler.execute(Data, column, reference_column, position)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "Monetary": [100.0, 200.0], "Recency": [534, 112],
                                    "T": [534, 112], "Frequency": [1, 1]})
    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """

    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112],
                         "Frequency": [1, 1], "Monetary": [100.0, 200.0]})
    column = 'id_customer'
    reference_column = 'Monetary'
    position = 'After'
    result = execution_handler.execute(Data, column, reference_column, position)
    expected_result = pd.DataFrame({"Recency": [534, 112], "T": [534, 112], "Frequency": [1, 1],
                                    "Monetary": [100.0, 200.0], "id_customer": [0, 1]})
    pd.testing.assert_frame_equal(result, expected_result)
