import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.string_column_replace_null.python.ExecutionHandler import ExecutionHandler

def test_string_replace_null():
    df = pd.DataFrame({'x': ["jon", "app", "mark", None]})

    handler = ExecutionHandler()
    df = handler.execute(df, 'x', "invalid")

    expected = pd.DataFrame({'x': ["jon", "app", "mark", "invalid"]})
    pd.testing.assert_frame_equal(expected, df)

