import pandas as pd
import numpy as np
from applications.HyperPersonalizationApplication.code.ActionDefinition.scatter_plot.python.ExecutionHandler import \
    ExecutionHandler


def test_scatter_plot():
    execution_handler = ExecutionHandler()
    segment_data = pd.DataFrame({"User ID": [0, 1, 2],
                                 "segment": [1, 0, 1],
                                 "col1": [1, 1, 0],
                                 "col2": [0, 0, 1]})
    segment_column = 'segment'
    customer_id_column = 'User ID'
    result = execution_handler.execute(segment_data, customer_id_column, segment_column)
    expected_result = pd.DataFrame({"index": [0, 1, 2],
                                    0: [np.nan, 8.396257e-17, np.nan], 1: [-8.226965e-17, np.nan, 8.464560e-19],
                                    "col2 (Feature 1)": [-0.471405, -0.471405, 0.942809]})
    assert(result.values, expected_result.values)
    #pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
