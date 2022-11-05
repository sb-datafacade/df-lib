import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_isnumeric.python.ExecutionHandler import ExecutionHandler



def test_validate_string_isnumeric():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['10', "15", "20", "25", "3o"]})
    columns = ['col1']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['10', "15", "20", "25", "3o"],
                                    'col1_valid_isnum': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
