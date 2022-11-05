import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.find_and_replace_substring.python.ExecutionHandler import ExecutionHandler



def test_find_and_replace_substring():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    Data = pd.DataFrame({"col1": ['gain', "main", "chain", "maintain", "ant"]})
    find_str = 'ain'
    replace_str = '000'
    result = execution_handler.execute(Data, find_str, replace_str)
    expected_result = pd.DataFrame({"col1": ['g000', 'm000', 'ch000', 'm000t000', 'ant']})

    pd.testing.assert_frame_equal(result, expected_result)

    """
    -case2
    """
    Data = pd.DataFrame({"col1": ['gain', "main", "chain", "maintain", "ant"]})
    columns = ['col1']
    find_str = 'ain'
    replace_str = '000'
    result = execution_handler.execute(Data, find_str, replace_str, columns)
    expected_result = pd.DataFrame({"col1": ['gain', "main", "chain", "maintain", "ant"],
                                    'col1_replaced': ['g000', 'm000', 'ch000', 'm000t000', 'ant']})

    pd.testing.assert_frame_equal(result, expected_result)
