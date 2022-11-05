import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.similarity_encode.python.ExecutionHandler import ExecutionHandler


def test_similarity_encode():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col2': ['john', 'mac', 'jon', 'mak']})
    columns = ['col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({'col2': ['john', 'mac', 'jon', 'mak'],
                                    'new_col2': [[1.0, 0.23529411764705882, 0.0, 0.0],
                                                 [0.0, 0.0, 1.0, 0.2],
                                                 [0.23529411764705882, 1.0, 0.0, 0.0],
                                                 [0.0, 0.0, 0.2, 1.0]]})
    pd.testing.assert_frame_equal(result, expected_result)
