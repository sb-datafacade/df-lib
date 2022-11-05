import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.transform_to_lower_case.python.ExecutionHandler import ExecutionHandler


def test_transform_lower_case():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"col1": ['TEST', "Train"],
                         "col2": ['t', "TRaIn"]})
    columns = ['col1','col2']
    result = execution_handler.execute(Data, columns)
    expected_result = pd.DataFrame({"col1": ['test', "train"],
                                    'col2': ['t', 'train']})

    pd.testing.assert_frame_equal(result, expected_result)