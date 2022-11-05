import pandas as pd
from applications.HyperPersonalizationApplication.code.ActionDefinition.customer_segment_profiling.python.ExecutionHandler import \
    ExecutionHandler


def test_customer_segment_profiling():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": [534, 235, 534], "col2": [534, 112, 534], 'gender': ['M', 'F', 'M'], "segment": [1, 2, 1],
                         'name': ['jack', 'jenny', 'roy']})
    segment_column = 'segment'
    CustomerId = ['name']
    result = execution_handler.execute(Data, CustomerId, segment_column)
    expected_result = pd.DataFrame({"segment": [1, 2, 'population'], "col1": [534, 235, 384.0],
                                    "col2": [534, 112, 323.0], 'gender': ['M', 'F', 'M']})
    pd.testing.assert_frame_equal(result, expected_result)