import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.validate_string_length.python.ExecutionHandler import ExecutionHandler



def test_validate_string_length():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['tan', "pan", "can", "nan", "tangent"]})
    columns = ['col1']
    ends_with = 3
    result = execution_handler.execute(Data, ends_with, columns)
    expected_result = pd.DataFrame({"col1": ['tan', "pan", "can", "nan", "tangent"],
                                    'col1_valid_length': [True, True, True, True, False]})

    pd.testing.assert_frame_equal(result, expected_result)
