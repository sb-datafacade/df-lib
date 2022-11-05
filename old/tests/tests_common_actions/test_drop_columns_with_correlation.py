import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.drop_columns_with_correlation.python.ExecutionHandler import ExecutionHandler


def test_drop_columns_with_correlation():
    handler = ExecutionHandler()

    df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 2, 3], 'z': [1, 2, 3]})
    new_df = handler.execute(df, threshold_correlation=0.95)

    expected = pd.DataFrame({'x': [1, 2, 3]})

    pd.testing.assert_frame_equal(new_df, expected)
