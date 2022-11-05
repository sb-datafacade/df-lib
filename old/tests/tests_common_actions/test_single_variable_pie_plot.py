import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.single_variable_pie_plot.python.ExecutionHandler import ExecutionHandler

def test_single_variable_pie_plot():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50]})
    axis = 'col1'
    sql_filter = 'optional'
    summary_type = 'Count'
    result = execution_handler.execute(Data, axis, sql_filter, summary_type).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col1': ['E', 'A', 'C'],
                                    'Count': [4, 3, 1]})
    pd.testing.assert_frame_equal(result, expected_result)
    """
    -case2
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50]})
    axis = 'col1'
    sql_filter = 'optional'
    summary_type = 'Count Percentage'
    result = execution_handler.execute(Data, axis, sql_filter, summary_type).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col1': ['E', 'A', 'C'],
                                    'Count Percentage': [50, 37.5, 12.5]})
    pd.testing.assert_frame_equal(result, expected_result)