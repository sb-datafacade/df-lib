import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.assemble_vectors.python.ExecutionHandler import ExecutionHandler

def test_assemble_vectors():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id": [np.array([0, 1])], "int_id": [np.array([0, 1])], "value": [np.array([0, 1])]})
    columns = ['id', 'int_id', 'value']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"id": [np.array([0, 1])], "int_id": [np.array([0, 1])],
                                    "value": [np.array([0, 1])], 'assembled_column': [np.array([[0, 1], [0, 1], [0, 1]])]})
    pd.testing.assert_frame_equal(result, expected_result)
