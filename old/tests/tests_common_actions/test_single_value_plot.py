import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.single_value_plot.python.ExecutionHandler import ExecutionHandler

def test_single_value_plot():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50, 5]})
    variable_name = 'col1'
    sql_filter = 'optional'
    single_value_name = 'optional'
    value_type = 'Count'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Count Of col1 Is 9'
    assert result == expected_result

    """
    -case2
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'col2': [10, 20, 10, 20, 30, 30, 40, 50, 5]})
    variable_name = 'col1'
    sql_filter = 'optional'
    single_value_name = 'optional'
    value_type = 'Unique Count'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Unique Count Of col1 Is 4'
    assert result == expected_result

    """
    -case3
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'Age': [10, 20, 10, 20, 30, 30, 40, 40, 40]})
    variable_name = 'Age'
    sql_filter = 'optional'
    single_value_name = 'Average Age'
    value_type = 'Average'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Average Age Is 26.67'
    assert result == expected_result

    """
    -case4
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'Age': [10, 20, 10, 20, 30, 30, 50, 40, 40]})
    variable_name = 'Age'
    sql_filter = 'optional'
    single_value_name = 'Maximum Age'
    value_type = 'Maximum'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Maximum Age Is 50'
    assert result == expected_result

    """
    -case5
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'Age': [10, 20, 10, 20, 30, 30, 50, 40, 40]})
    variable_name = 'Age'
    sql_filter = 'optional'
    single_value_name = 'Minimum Age'
    value_type = 'Minimum'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Minimum Age Is 10'
    assert result == expected_result

    """
    -case6
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'Age': [10, 20, 10, 20, 30, 30, 50, 40, 40]})
    variable_name = 'Age'
    sql_filter = 'optional'
    single_value_name = 'Median Age'
    value_type = 'Median'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Median Age Is 30.0'
    assert result == expected_result

    """
    -case7
    """
    Data = pd.DataFrame({'col1': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C', 'D'],
                         'Age': [10, 20, 10, 20, 30, 30, 50, 40, 40]})
    variable_name = 'Age'
    sql_filter = 'optional'
    single_value_name = 'Total Age'
    value_type = 'Total'
    result = execution_handler.execute(Data, variable_name, sql_filter, single_value_name, value_type)
    expected_result = 'Total Age Is 250'
    assert result == expected_result
