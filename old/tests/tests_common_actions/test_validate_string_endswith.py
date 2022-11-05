import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_endswith.python.ExecutionHandler import ExecutionHandler



def test_validate_string_endswith():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['tan', "pan", "can", "nan", "ant"]})
    columns = ['col1']
    ends_with = 'an'
    result = execution_handler.execute(Data, ends_with, columns)
    expected_result = pd.DataFrame({"col1": ['tan', "pan", "can", "nan", "ant"],
                                    'col1_valid_endswith': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
