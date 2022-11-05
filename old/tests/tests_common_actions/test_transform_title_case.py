import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.transform_to_title_case.python.ExecutionHandler import ExecutionHandler


def test_transform_title_case():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['TEST', "TrAiN"],
                         "col2": ['tEsT', "TRaIn"]})
    columns = ['col1','col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['Test', "Train"],
                                    'col2': ['Test', 'Train']})

    pd.testing.assert_frame_equal(result, expected_result)