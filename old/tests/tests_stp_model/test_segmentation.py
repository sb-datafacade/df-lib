import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.segmentation.python.ExecutionHandler import \
    ExecutionHandler


def test_segmentation():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id": ['1121', '1212'], "name": ['jack', "roy"], "col1": [534, 534], "col2": [534, 534],
                         "col3": [1, 2], 'education': ['graduate', 'post-grad']})
    """
    -case1
    """
    method = 'Kmeans'
    number_of_segments = 2
    CustomerID = ['id', 'name']
    result = execution_handler.execute(Data, CustomerID, method, number_of_segments)
    expected_result = pd.DataFrame({"id": ['1121', '1212'], "name": ['jack', "roy"],
                                    "col1": [534, 534], "col2": [534, 534], "col3": [1, 2],
                                    'education': ['graduate', 'post-grad'], 'segment': [0, 1]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [534, 534], "col2": [534, 534], "col3": [1, 2], 'education': ['graduate', 'post-grad']})
    method = 'Hierarchical/Agglomerative'
    number_of_segments = 2
    CustomerID = []
    result = execution_handler.execute(Data, CustomerID, method, number_of_segments)
    expected_result = pd.DataFrame({"ID": [1, 2], "col1": [534, 534], "col2": [534, 534], "col3": [1, 2],
                                    'education': ['graduate', 'post-grad'], 'segment': [1, 0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)

    """
    -case3
    """
    Data = pd.DataFrame({"col1": [534, 534], "col2": [534, 534], "col3": [1, 2], 'education': ['graduate', 'post-grad'],})
    method = 'Gaussian Mixture Model'
    number_of_segments = 2
    CustomerID = []
    result = execution_handler.execute(Data, CustomerID, method, number_of_segments)
    expected_result = pd.DataFrame({"ID": [1, 2], "col1": [534, 534], "col2": [534, 534], "col3": [1, 2],
                                    'education': ['graduate', 'post-grad'], 'segment': [0, 1]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
