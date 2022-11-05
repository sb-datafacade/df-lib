import numpy as np
import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.extract_using_regex.python.ExecutionHandler import ExecutionHandler



def test_extract_using_regex():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['my cat ate the plum', 'my cat ate 2 plums', 'my car at 3 slums',
                                  'my car at the slums', 'my cat ate 5 plums']})
    columns = ['col1']
    expression = 'my ca[rt] ate? (the|[2-4]) [sp]lums?'
    result = execution_handler.execute(Data,  expression, columns)
    expected_result = pd.DataFrame({"col1": ['my cat ate the plum', 'my cat ate 2 plums', 'my car at 3 slums',
                                             'my car at the slums', 'my cat ate 5 plums'],
                                    'col1_extracted': ['the', '2', '3', 'the', np.nan]})

    pd.testing.assert_frame_equal(result, expected_result)
