import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.rfm_segmentation.python.ExecutionHandler import \
    ExecutionHandler

def test_rfm_segment():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112], "Frequency": [1, 1],
                         "Monetary.min": [100, 200], "Monetary.avg": [100, 200], "Monetary.max": [100, 200],
                         "Monetary": [100.0, 200.0]})
    rfm_table = Data
    recency_column = "Recency"
    frequency_column = "Frequency"
    monetary_value_column = "Monetary"
    result = execution_handler.execute(rfm_table, recency_column, frequency_column, monetary_value_column)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 112], "T": [534, 112], "Frequency": [1, 1],
                                    "Monetary.min": [100, 200], "Monetary.avg": [100.0, 200.0],
                                    "Monetary.max": [100, 200],
                                    "Monetary": [100.0, 200.0], 'R': [1, 3], 'F': [1, 1], 'M': [3, 3],
                                    'RFM_Score': [5, 7], 'RFM_Segment': ['113', '313'],
                                    'Segment': ['Lost Customer', 'Big Spender']})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
