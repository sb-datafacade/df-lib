import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.extract_before_after_delimiter.python.ExecutionHandler import \
    ExecutionHandler


def test_extract_before_after_delimiter():
    execution_handler = ExecutionHandler()

    """
    -case1
    """
    Data = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                         "col2": ['//,123,follow', '123//']})
    columns = ['col1', 'col2']
    delimiter = ","
    position = "Before"
    result = execution_handler.execute(Data, columns, delimiter, position)
    expected_result = pd.DataFrame({"col1": ['112*,hello,112', "**,world,**,*"],
                                    "col2": ['//,123,follow', '123//'],
                                    'extract_col1': ['112*', '**'],
                                    'extract_col2': ['//', 'None']})
    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": ['112*,hello', "**,world"],
                         "col2": ['//,123', '123//']})
    columns = ['col1', 'col2']
    delimiter = ","
    position = "After"
    result = execution_handler.execute(Data, columns, delimiter, position)
    expected_result = pd.DataFrame({"col1": ['112*,hello', "**,world"],
                                    "col2": ['//,123', '123//'],
                                    'extract_col1': ['hello', 'world'],
                                    'extract_col2': ['123', 'None']})
    pd.testing.assert_frame_equal(result, expected_result)
