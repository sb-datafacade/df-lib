import pandas as pd
import numpy as np
from applications.DataFacadeOOB.code.ActionDefinition.explode_array.python.ExecutionHandler import ExecutionHandler

def test_explode_array():
    execution_handler = ExecutionHandler()
    Data=pd.DataFrame({'col1':[np.array(["A",'b']),np.array(["A",'b'])],
                       'col2':[np.array(["A",'b']),np.array(["A",'b'])]})
    columns=['col1','col2']
    result = execution_handler.execute(Data,columns)
    expected_result = pd.DataFrame({'col1': ['A','A','b','b','A','A','b','b'],
                                    'col2': ['A','b','A','b','A','b','A','b']})
    pd.testing.assert_frame_equal(result, expected_result)

