import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_isalpha.python.ExecutionHandler import ExecutionHandler



def test_validate_string_isalpha():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['ant', "bat", "cat", "boat", "1252"]})
    columns = ['col1']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['ant', "bat", "cat", "boat", "1252"],
                                    'col1_valid_isalpha': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
