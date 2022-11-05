import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.segment_difference_in_profiles.python.ExecutionHandler import \
    ExecutionHandler


def test_segment_difference():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [100, 200, 300, 400], "col2": [400, 300, 200, 100], "segment": [1, 2, 1, 2],
                         'name': ['jack', 'jenny', 'roy', 'sam'], 'gender': ['M', 'F', 'M', 'M']})
    segment_column = 'segment'
    CustomerId = ['name']
    result = execution_handler.execute(Data, CustomerId, segment_column)
    expected_result = pd.DataFrame({"segment": [1, 2], "col1": [0, 1],
                                    "col2": [1, 0]})
    pd.testing.assert_frame_equal(result, expected_result)
    """
    -case2
    """
    Data = pd.DataFrame({"col1": [100, 200, 300, 400], "col2": [400, 300, 200, 100], "segment": [1, 2, 1, 2],
                         'ID': ['jack', 'jenny', 'roy', 'sam'], 'gender': ['M', 'F', 'M', 'M']})
    segment_column = 'segment'
    CustomerId = []
    result = execution_handler.execute(Data, CustomerId, segment_column)
    expected_result = pd.DataFrame({"segment": [1, 2], "col1": [0, 1],
                                    "col2": [1, 0]})
    pd.testing.assert_frame_equal(result, expected_result)
