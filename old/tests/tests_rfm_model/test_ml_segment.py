import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.ml_segmentation.python.ExecutionHandler import \
    ExecutionHandler


def test_ML_segment():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 534], "T": [534, 534], "Frequency": [1, 2],
                         "Monetary.min": [100, 100], "Monetary.avg": [100, 100], "Monetary.max": [100, 100],
                         "Monetary": [100.0, 100.0], "name": ['jack', 'roy']})
    id_customer = ["id_customer", "name"]
    Number_Of_Segments = 2
    result = execution_handler.execute(Data, id_customer, Number_Of_Segments)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "Recency": [534, 534],
                                    "T": [534, 534], "Frequency": [1, 2],
                                    "Monetary.min": [100, 100], "Monetary.avg": [100, 100], "Monetary.max": [100, 100],
                                    "Monetary": [100.0, 100.0], "name": ['jack', 'roy'], 'Segment': [2, 1]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
