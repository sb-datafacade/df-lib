import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.two_d_single_axis_summary_plot.python.ExecutionHandler import ExecutionHandler

def test_two_d_single_axis_summary_plot():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50]})
    axis = 'col1'
    value = 'col2'
    sql_filter = 'optional'
    value_type = 'Total'
    result = execution_handler.execute(Data, axis, value, sql_filter, value_type).reset_index().drop('index',axis=1)
    expected_result = pd.DataFrame({'col1': ['E', 'A', 'C'],
                                    'col2 Total': [100, 60, 50]})
    pd.testing.assert_frame_equal(result, expected_result)
    """
    -case2
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50]})
    axis = 'col1'
    value = 'col2'
    sql_filter = 'optional'
    value_type = 'Count Percentage'
    result = execution_handler.execute(Data, axis, value, sql_filter, value_type).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col1': ['E', 'A', 'C'],
                                    'col2 Count Percentage': [50, 37.5, 12.5]})
    pd.testing.assert_frame_equal(result, expected_result)