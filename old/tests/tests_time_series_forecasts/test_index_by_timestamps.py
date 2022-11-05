import math

import pandas as pd
from applications.TimeSeriesForecast.code.ActionDefinition.IndexByTimeStamps.python.ExecutionHandler import ExecutionHandler


def test_index_by_timestamps():
    df = pd.DataFrame({
        'date': ['April 2021', 'April 2022', 'March 2022'],
        'value': [22, 23, 24],
        'dimension': ['a', 'b', 'c']
    })

    handler = ExecutionHandler()
    new_df = handler.execute(df=df, primary_dimension_column='dimension', target_columns=['value'], timestamp_column='date')

    expected = pd.DataFrame({
        'date': ['April 2021', 'April 2022', 'March 2022'],
        'a_value': [22, math.nan, math.nan],
        'b_value': [math.nan, 23, math.nan],
        'c_value': [math.nan, math.nan, 24]
    })

    expected = expected.set_index('date')

    pd.testing.assert_frame_equal(new_df, expected)
