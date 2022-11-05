import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.two_variable_single_axis_date_time_summary_plot.python.ExecutionHandler import \
    ExecutionHandler


def test_two_variable_single_axis_date_time_summary_plot():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame(
        {'transaction_date': ['01/01/2018', '01/09/2018', '01/05/2018', '01/03/2018', '02/01/2018', '08/02/2018',
                              '12/05/2018', '15/03/2018'],
         'unit': [10, 20, 10, 20, 30, 30, 40, 50],
         'gender': ['male', 'male', 'male', 'female', 'female', 'female', 'female', 'male']})
    date_time_axis = 'transaction_date'
    value = 'unit'
    legend = 'gender'
    date_time_frequency = 'Months'
    sql_filter = 'optional'
    value_type = 'Total'
    result = execution_handler.execute(Data, date_time_axis, legend, value, date_time_frequency, sql_filter, value_type)
    expected_result = pd.DataFrame({'Months': ['2018-01', '2018-02', '2018-03', '2018-08', '2018-12'],
                                    'female': [20.0, 30.0, 0, 30, 40],
                                    'male': [40.0, 0, 50.0, 0, 0]})
    np.array_equal(result.values, expected_result.values)
    """
       -case2
       """
    Data = pd.DataFrame(
        {'transaction_date': ['01/01/2018', '01/09/2018', '01/05/2018', '01/03/2018', '02/01/2018', '08/02/2018',
                              '12/05/2018', '15/03/2018'],
         'unit': [10, 20, 10, 20, 30, 30, 40, 50],
         'gender': ['male', 'male', 'male', 'female', 'female', 'female', 'female', 'male']})
    date_time_axis = 'transaction_date'
    value = 'unit'
    legend = 'gender'
    date_time_frequency = 'Months'
    sql_filter = 'optional'
    value_type = 'Count Percentage'
    result = execution_handler.execute(Data, date_time_axis, legend, value, date_time_frequency, sql_filter, value_type)
    expected_result = pd.DataFrame({'Months': ['2018-01', '2018-02', '2018-03', '2018-08', '2018-12'],
                                    'female': [12.5, 12.5, 0, 12.5, 12.5],
                                    'male': [37.5, 0, 12.5, 0, 0]})
    np.array_equal(result.values, expected_result.values)
