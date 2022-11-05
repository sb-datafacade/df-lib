import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_isalphanumeric.python.ExecutionHandler import ExecutionHandler



def test_validate_string_isalphanumeric():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['10T', "15T", "T20", "L25", "??"]})
    columns = ['col1']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['10T', "15T", "T20", "L25", "??"],
                                    'col1_valid_isalphanum': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
