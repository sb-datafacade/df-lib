import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.split_string_by_delimiter.python.ExecutionHandler import ExecutionHandler


def test_split_string_by_delimiters():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['1,hello,1', "*,world,*"]})
    columns = ['col1']
    delimiter = ","
    result = execution_handler.execute(Data, columns, delimiter)
    expected_result = pd.DataFrame({"col1": ['1,hello,1', "*,world,*"],
                                    "col1_0": ['1', '*'],
                                    'col1_1': ['hello', 'world'],
                                    'col1_2': ['1', '*']})

    pd.testing.assert_frame_equal(result, expected_result)