import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.segment_description.python.ExecutionHandler import \
    ExecutionHandler


def test_segment_description():
    execution_handler = ExecutionHandler()
    segment_data = pd.DataFrame({"ID": [101, 109, 110, 132], "segment": [0, 1, 1, 0]})
    Data = pd.DataFrame({"ID": [101, 109, 110, 132], "name": ['jack', 'roy', 'mac', 'sid'],
                         "col1": [10.2, 20.0, 35.5, -23.6], "col2": [400, 300, 200, 100]})
    """
    -case1
    """
    segment_data = segment_data
    CustomerID = ['ID', 'name']
    segment_column = 'segment'
    descriptor_data = Data
    method = 'Logistic Regression'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 1, 1, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case2
    """
    segment_data = segment_data
    CustomerID = ['ID', 'name']
    segment_column = 'segment'
    descriptor_data = Data
    method = 'Decision Tree Classifier'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 1, 1, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case3
    """
    segment_data = segment_data
    CustomerID = ['ID', 'name']
    segment_column = 'segment'
    descriptor_data = Data
    method = 'Random Forest Classifier'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 1, 1, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case4
    """
    Data = pd.DataFrame({"col1": [10.2, 20.0, 35.5, -23.6], "col2": [400, 300, 200, 100]})
    segment_data = segment_data
    CustomerID = []
    segment_column = 'segment'
    descriptor_data = Data
    method = 'XGBoost Classifier'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 0, 0, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
