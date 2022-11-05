import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.segmentation_summary.python.ExecutionHandler import \
    ExecutionHandler


def test_segmentation_summary():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": [534, 534, 235], "col2": [534, 534, 235], "segment": [1, 2, 1]})
    segment_column = 'segment'
    result = execution_handler.execute(Data, segment_column)
    expected_result = pd.DataFrame({"Segment": ['Segment 2', 'Segment 3'], "Segment Count": [2, 1]})
    pd.testing.assert_frame_equal(result, expected_result)
