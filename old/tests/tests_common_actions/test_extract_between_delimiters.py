import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.extract_between_delimiters.python.ExecutionHandler import ExecutionHandler

def test_extract_between_delimiters():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                         "col2": ['//,123,follow', ',123,//']})
    columns = ['col1', 'col2']
    left_delimiter = ","
    right_delimiter = ","
    result = execution_handler.execute(Data, columns, left_delimiter, right_delimiter)
    expected_result = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                                    "col2": ['//,123,follow', ',123,//'],
                                    'extract_col1': ['hello', 'world'],
                                    'extract_col2': ['123', '123']})
    pd.testing.assert_frame_equal(result, expected_result)
