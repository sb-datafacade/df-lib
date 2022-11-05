import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.merge_table.python.ExecutionHandler import \
    ExecutionHandler


def test_merge_table():
    execution_handler = ExecutionHandler()
    df1 = pd.DataFrame(
        {"id": [121, 212, 321, 412], "date": ['10/12/2022', '12/08/2021', '08/02/2022', '23/05/2022'],
         "int_id": [100, 112, 231, 325], "value": [0.25, 1.28, 2.25, 3.26]})
    df2 = pd.DataFrame({"customer_id": [121, 212, 321, 412],
                        "name": ['Michale', 'Vicky', 'Kary', 'Anna'], "age": [25, 28, 35, 26]})
    df1_key = "id"
    df2_key = "customer_id"
    join_type = "left"
    expected_result = pd.DataFrame(
        {"id": [121, 212, 321, 412], "date": ['10/12/2022', '12/08/2021', '08/02/2022', '23/05/2022'],
         "int_id": [100, 112, 231, 325], "value": [0.25, 1.28, 2.25, 3.26], "customer_id": [121, 212, 321, 412],
         "name": ['Michale', 'Vicky', 'Kary', 'Anna'], "age": [25, 28, 35, 26]})
    result = execution_handler.execute(df1, df2, df1_key, df2_key, join_type)
    pd.testing.assert_frame_equal(result, expected_result)
