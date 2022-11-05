import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.out_of_sample_prediction.python.ExecutionHandler import \
    ExecutionHandler


def test_out_of_sample_prediction():
    execution_handler = ExecutionHandler()
    segment_data = pd.DataFrame({"ID": [101, 109, 110, 132], "segment": [0, 1, 1, 0]})
    Data = pd.DataFrame({"col1": [10.2, 20.0, 35.5, -23.6], "col2": [400, 300, 200, 100],
                         "col3": [10.2, 20.0, 35.5, -23.6]})
    out_of_sample_data = pd.DataFrame({"col1": [10.2, -23.6], "col2": [400, 100]})
    """
    -case1
    """
    segment_data = segment_data
    CustomerID = []
    segment_column = 'segment'
    descriptor_data = Data
    out_of_sample_data = out_of_sample_data
    method = 'Logistic Regression'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method, out_of_sample_data)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.2, 20.0, 35.5, -23.6], "col2": [400, 300, 200, 100],
                         "col3": [10.2, 20.0, 35.5, -23.6], "name": ['jack', 'roy', 'mac', 'sid']})
    out_of_sample_data = pd.DataFrame({"col1": [10.2, -23.6], "col2": [400, 100], "name": ['sam', 'rudy']})
    segment_data = segment_data
    segment_column = 'segment'
    descriptor_data = Data
    CustomerID = ['name']
    method = 'Decision Tree Classifier'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method, out_of_sample_data)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case3
    """
    Data = pd.DataFrame({"col1": [10.2, 20.0, 35.5, -23.6], "col2": [400, 300, 200, 100],
                         "col3": [10.2, 20.0, 35.5, -23.6], "name": ['jack', 'roy', 'mac', 'sid'],
                         "id": ['12145', '21150', '12365', '12358']})
    out_of_sample_data = pd.DataFrame({"col1": [10.2, -23.6], "col2": [400, 100], "name": ['sam', 'rudy']})
    segment_data = segment_data
    segment_column = 'segment'
    CustomerID = ['name', 'id']
    descriptor_data = Data
    method = 'Random Forest Classifier'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method, out_of_sample_data)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case4
    """
    Data = pd.DataFrame({"col1": [10.2, 20.0, 35.5, -23.6], "col2": [400, 300, 200, 100],
                         "col3": [10.2, 20.0, 35.5, -23.6], "name": ['jack', 'roy', 'mac', 'sid'],
                         "id": ['12145', '21150', '12365', '12358']})
    out_of_sample_data = pd.DataFrame({"col1": [10.2, -23.6], "col2": [400, 100]})
    segment_data = segment_data
    segment_column = 'segment'
    CustomerID = ['name', 'id']
    descriptor_data = Data
    method = 'XGBoost Classifier'
    result = execution_handler.execute(segment_data, CustomerID, segment_column, descriptor_data, method, out_of_sample_data)
    result = pd.DataFrame(result['Predicted'])
    expected_result = pd.DataFrame({"Predicted": [0, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
