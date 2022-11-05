import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_startswith.python.ExecutionHandler import ExecutionHandler



def test_validate_string_startswith():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['go', "gone", "goes", "going", "went"]})
    columns = ['col1']
    starts_with = 'go'
    result = execution_handler.execute(Data, starts_with, columns)
    expected_result = pd.DataFrame({"col1": ['go', "gone", "goes", "going", "went"],
                                    'col1_valid_startswith': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
