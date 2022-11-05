import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.numeric_column_scaling.python.ExecutionHandler import \
    ExecutionHandler


def test_scale_values():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55, 10.55],
                         "col2": [10, 30, 30, 30],
                         "col3": [10, 20, 30, 40]})
    result = execution_handler.execute(Data)
    expected_result = pd.DataFrame({"col1": [0.967391, 0.0, 0.130435, 1],
                                    "col3": [0.0, 0.33, 0.67, 1],
                                    "col2_10": [1, 0, 0, 0],
                                    "col2_30": [0, 1, 1, 1]
                                    })

    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)