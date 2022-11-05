import pandas as pd

from applications.DataFacadeOOB.code.ActionDefinition.remove_duplicate_columns.python.ExecutionHandler import ExecutionHandler


def test_remove_duplicate_columns():
    handler = ExecutionHandler(mode="testing")

    df = pd.DataFrame({
        'x': [1, 2, 3],
        'x1': [1, 2, 3],
        'y': ['a', 'b', 'c'],
        'y1': ['a', 'b', 'c']
    })

    df = handler.execute(df)
    expected_df = pd.DataFrame({
        'x': [1, 2, 3],
        'y': ['a', 'b', 'c']
    })

    assert df.to_json() == expected_df.to_json()
