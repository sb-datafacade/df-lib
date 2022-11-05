import pandas as pd
from applications.HyperPersonalizationApplication.code.ActionDefinition.customer_frequency_summary_plot.python.ExecutionHandler import \
    ExecutionHandler
from tests.helpers import load_data

def test_customer_frequency_summary_plots():
    execution_handler = ExecutionHandler()
    Data = load_data("customer_segments.csv")
    data = Data
    axis = "AGE"
    legend = "Segment"
    sql_filter = 'optional'
    number_of_class = 6
    result = execution_handler.execute(data, axis, legend, sql_filter, number_of_class)
    expected_result = pd.pivot_table(data, index=axis, values=data.columns[0],
                                     columns=[legend], aggfunc='count').fillna(0).reset_index()

    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
