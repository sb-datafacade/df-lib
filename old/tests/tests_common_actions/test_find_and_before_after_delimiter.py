import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.find_and_replace_before_after_delimiter.python.ExecutionHandler import ExecutionHandler


def test_find_and_before_after_delimiter():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                         "col2": ['//,123,follow', ',123,//']})
    columns = ['col1', 'col2']
    delimiter = ","
    position = "After"
    substring = 'test'
    result = execution_handler.execute(Data, columns, substring, delimiter, position)
    expected_result = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                                    "col2": ['//,123,follow', ',123,//'],
                                    'new_col1': ['112*,test', "**,test"],
                                    'new_col2': ['//,test', ',test']})
    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                         "col2": ['//,123,follow', '123']})
    columns = ['col1', 'col2']
    delimiter = ","
    position = "Before"
    substring = 'test'
    result = execution_handler.execute(Data, columns, substring, delimiter, position)
    expected_result = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                                    "col2": ['//,123,follow', '123'],
                                    'new_col1': ['test,hello,112', "test,world,**,*"],
                                    'new_col2': ['test,123,follow', 'None']})
    pd.testing.assert_frame_equal(result, expected_result)
