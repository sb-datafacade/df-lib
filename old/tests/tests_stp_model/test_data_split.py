import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.data_split.python.ExecutionHandler import ExecutionHandler

def test_data_split():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55], "col2": [10.25, 1.35, 2.55],
                         "col3": [10.25, 1.35, 2.55], "col4": [10.25, 1.35, 2.55]})
    columns = ['col1', 'col4']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55], "col4": [10.25, 1.35, 2.55]})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": [10.25, 1.35, 2.55], "col2": [10.25, 1.35, 2.55],
                         "col3": [10.25, 1.35, 2.55], "col4": [10.25, 1.35, 2.55]})
    columns = []
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": [10.25, 1.35, 2.55], "col2": [10.25, 1.35, 2.55],
                                    "col3": [10.25, 1.35, 2.55], "col4": [10.25, 1.35, 2.55]})

    pd.testing.assert_frame_equal(result, expected_result)