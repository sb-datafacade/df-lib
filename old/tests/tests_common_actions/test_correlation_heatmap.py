import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.correlation_heat_map.python.ExecutionHandler import ExecutionHandler


def test_correlation_heatmap():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": [0.2, 0.3], "col2": [0.3, 0.2]})
    columns = ['col1', 'col2']
    expected_result = pd.DataFrame({"index": ['col1', 'col2'], "col1": [1.0, -1.0], "col2": [-1.0, 1.0]})
    result = execution_handler.execute(Data, columns)
    pd.testing.assert_frame_equal(result, expected_result)
