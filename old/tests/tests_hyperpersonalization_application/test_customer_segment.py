import pandas as pd
from applications.HyperPersonalizationApplication.code.ActionDefinition.customer_segmentation.python.ExecutionHandler import \
    ExecutionHandler
from tests.helpers import load_data


def test_customer_segment():
    execution_handler = ExecutionHandler()
    data = load_data("customer_segments.csv")
    data = data[data.columns[0:6]][0:4]
    propensity_data = load_data("propensity_data.csv")[0:4]
    CustomerID = 'User ID'
    location = ['GUJARAT']
    number_of_segments = 4
    result = execution_handler.execute(propensity_data, data, CustomerID, location, number_of_segments)
    table = data[data.columns[0:6]][0:4]
    table['Segment'] = [0, 1, 0, 1]
    expected_result = table.reset_index()
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
