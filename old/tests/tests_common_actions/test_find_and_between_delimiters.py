import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.find_and_replace_between_delimiters.python.ExecutionHandler import ExecutionHandler


def test_find_and_between_delimiters():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                         "col2": ['//,123,follow', ',123,//']})
    columns = ['col1', 'col2']
    left_delimiter = ","
    right_delimiter = ","
    substring = 'test'
    result = execution_handler.execute(Data, columns, substring, left_delimiter, right_delimiter)
    expected_result = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                                    "col2": ['//,123,follow', ',123,//'],
                                    'new_col1': ['112*,test,112', "**,test,**,*"],
                                    'new_col2': ['//,test,follow', ',test,//']})
    pd.testing.assert_frame_equal(result, expected_result)
