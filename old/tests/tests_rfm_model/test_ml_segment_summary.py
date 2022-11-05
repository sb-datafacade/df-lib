import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.ml_segmentation_summary.python.ExecutionHandler import \
    ExecutionHandler


def test_ml_segment_summary():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"Segment": [0, 1], "Recency": [534, 534], "T": [534, 534], "Frequency": [1, 2],
                         "Monetary.min": [100, 100], "Monetary.avg": [100, 100], "Monetary.max": [100, 100],
                         "Monetary": [100.0, 100.0], "name": ['jack', 'roy']})
    ml_segment_data = Data
    recency_column = 'Recency'
    frequency_column = 'Frequency'
    monetary_value_column = 'Monetary'
    segment_column = 'Segment'
    result = execution_handler.execute(ml_segment_data, recency_column, frequency_column, monetary_value_column, segment_column)
    expected_result = pd.DataFrame({'Segment': ['Segment 0', 'Segment 1'], 'Recency(mean)': [534.0, 534.0], 'Frequency(mean)': [1, 2],
                                    'MonetaryValue(mean)': [100.0, 100], 'Segment count': [1, 1]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
