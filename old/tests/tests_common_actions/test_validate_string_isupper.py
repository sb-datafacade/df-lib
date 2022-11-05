import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_isupper.python.ExecutionHandler import ExecutionHandler



def test_validate_string_isupper():
    execution_handler= ExecutionHandler()
    Data = pd.DataFrame({"col1": ['ANT', "BOOK", "CAT", "TeSt", "TabLe"]})
    columns = ['col1']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['ANT', "BOOK", "CAT", "TeSt", "TabLe"],
                                    'col1_valid_isupper': [True, True, True, False, False]})

    pd.testing.assert_frame_equal(result, expected_result)
