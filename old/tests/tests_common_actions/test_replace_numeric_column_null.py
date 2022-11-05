import math
from applications.DataFacadeOOB.code.ActionDefinition.numeric_column_replace_null.python.ExecutionHandler import ExecutionHandler
import pandas as pd


def test_numeric_column_null():
    df = pd.DataFrame({
        'x': [1.2, 3.4, math.nan, 3.1]
    })

    handler = ExecutionHandler()
    df = handler.execute(df, 'x', 0.0)

    expected = pd.DataFrame({'x': [1.2, 3.4, 0.0, 3.1]})

    pd.testing.assert_frame_equal(expected, df)

