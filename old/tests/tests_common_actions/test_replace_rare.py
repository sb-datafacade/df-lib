import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.replace_rare.python.ExecutionHandler import ExecutionHandler


def test_replace_rare():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'D', 'D', 'D', 'E', 'F', 'G', 'G', 'E', 'E',
                                  'D', 'B', 'A']})
    column = 'col1'
    threshold_type = 'Absolute threshold'
    threshold_value = 2.0
    value = 'other'
    result = execution_handler.execute(Data, column, value, threshold_type, threshold_value)
    expected_result = pd.DataFrame({"col1": ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'other', 'D', 'D', 'D', 'E', 'other',
                                             'other', 'other', 'E', 'E', 'D', 'B', 'A']})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'D', 'D', 'D', 'E', 'F', 'G', 'G', 'E', 'E',
                                  'D', 'B', 'A']})
    column = 'col1'
    threshold_type = 'Fraction threshold'
    threshold_value = 0.1
    value = 'other'
    result = execution_handler.execute(Data, column, value, threshold_type, threshold_value)
    expected_result = pd.DataFrame({"col1": ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'other', 'D', 'D', 'D', 'E', 'other',
                                             'other', 'other', 'E', 'E', 'D', 'B', 'A']})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case3
    """
    Data = pd.DataFrame({"col1": ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'D', 'D', 'D', 'E', 'F', 'G', 'G', 'E', 'E',
                                  'D', 'B', 'A']})
    column = 'col1'
    threshold_type = 'Max common categories'
    threshold_value = 5.0
    value = 'other'
    result = execution_handler.execute(Data, column, value, threshold_type, threshold_value)
    expected_result = pd.DataFrame({"col1": ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'other', 'D', 'D', 'D', 'E', 'other',
                                             'other', 'other', 'E', 'E', 'D', 'B', 'A']})

    pd.testing.assert_frame_equal(result, expected_result)
