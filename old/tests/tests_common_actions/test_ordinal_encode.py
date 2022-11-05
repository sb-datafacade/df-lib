import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.ordinal_encode.python.ExecutionHandler import ExecutionHandler



def test_ordinal_encode():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({'col2': ['A', 'B', 'C', 'E']})
    columns = ['col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({'col2': ['A', 'B', 'C', 'E'],
                                    'col2_ordinal_encode': [0.0, 1.0, 2.0, 3.0]})

    pd.testing.assert_frame_equal(result, expected_result)
