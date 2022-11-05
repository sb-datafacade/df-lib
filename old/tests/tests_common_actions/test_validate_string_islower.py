import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_islower.python.ExecutionHandler import ExecutionHandler



def test_validate_string_islower():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['ant', "bat", "cat", "boat", "TabLe"]})
    columns = ['col1']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['ant', "bat", "cat", "boat", "TabLe"],
                                    'col1_valid_islower': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
