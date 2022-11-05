import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.single_variable_frequency_plot.python.ExecutionHandler import ExecutionHandler

def test_single_variable_frequency_plot():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50, 5]})
    axis = 'col2'
    sql_filter = 'optional'
    number_of_class = 5
    plot_type = 'Bar Chart'
    result = execution_handler.execute(Data, axis, sql_filter, number_of_class, plot_type).reset_index().drop('index', axis=1)
    expected_result = pd.DataFrame({'col2': ['(4.954, 14.0]', '(14.0, 23.0]', '(23.0, 32.0]', '(32.0, 41.0]', '(41.0, 50.0]'],
                                    'Frequency': [3, 2, 2, 1, 1]})
    pd.testing.assert_frame_equal(result, expected_result)
    """
    -case2
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50, 5]})
    axis = 'col2'
    sql_filter = 'optional'
    number_of_class = 5
    plot_type = 'Line Chart'
    result = execution_handler.execute(Data, axis, sql_filter, number_of_class, plot_type).reset_index().drop('index',
                                                                                                              axis=1)
    expected_result = pd.DataFrame(
        {'col2': ['(4.954, 14.0]', '(14.0, 23.0]', '(23.0, 32.0]', '(32.0, 41.0]', '(41.0, 50.0]'],
         'Frequency': [3, 2, 2, 1, 1]})
    pd.testing.assert_frame_equal(result, expected_result)
