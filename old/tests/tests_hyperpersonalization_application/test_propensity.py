import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.propensity_of_conversion.python.ExecutionHandler import \
    ExecutionHandler


def test_propensity():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1, 3, 4], "Recency": [53, 112, 54, 65], "Frequency": [1, 1, 2, 2],
                         "T": [53, 112, 54, 65], "Segment": [2, 2, 3, 3],
                         "Monetary": [100, 200, 300, 400], 'PC1': [0.1, 0.3, 0.2, -0.9],
                         'PC2': [1.1, 1.5, -1.9, 0.3]})
    Selected_Segment = 3
    Targeted_Segment = 2
    Number_Of_Points = 2
    result = execution_handler.execute(Data, Selected_Segment, Targeted_Segment, Number_Of_Points)
    expected_result = pd.DataFrame({"id_customer": [3, 4], "Recency": [54, 65], "Frequency": [2, 2],
                                    "T": [54, 65], "Segment": [3, 3],
                                    "Monetary": [300, 400], 'Propensity': [0.0, 0.573362]})[::-1]
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_result.reset_index(drop=True)
                                  , check_like=True)
