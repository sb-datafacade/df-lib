import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.two_variable_single_axis_summary_plot.python.ExecutionHandler import \
    ExecutionHandler


def test_two_variable_single_axis_summary_plot():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({'product': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C'],
                         'unit': [10, 20, 10, 20, 30, 30, 40, 50],
                         'gender': ['male', 'male', 'male', 'female', 'female', 'female', 'female', 'male']})
    axis = 'product'
    legend = 'gender'
    value = 'unit'
    sql_filter = 'optional'
    value_type = 'Total'
    result = execution_handler.execute(Data, axis, legend, value, sql_filter, value_type)
    expected_result = pd.DataFrame({'product': ['A', 'C', 'E'],
                                    'female': [30.0, 0, 90.0],
                                    'male': [30.0, 50, 10.0]})
    np.array_equal(result.values, expected_result.values)
    """
    -case2
    """
    Data = pd.DataFrame({'product': ['A', 'A', 'E', 'E', 'E', 'A', 'E', 'C'],
                         'unit': [10, 20, 10, 20, 30, 30, 40, 50],
                         'gender': ['male', 'male', 'male', 'female', 'female', 'female', 'female', 'male']})
    axis = 'product'
    legend = 'gender'
    value = 'unit'
    sql_filter = 'optional'
    value_type = 'Count Percentage'
    result = execution_handler.execute(Data, axis, legend, value, sql_filter, value_type)
    expected_result = pd.DataFrame({'product': ['A', 'C', 'E'],
                                    'female': [12.5, 0, 37.5],
                                    'male': [25, 12.5, 12.5]})
    np.array_equal(result.values, expected_result.values)
