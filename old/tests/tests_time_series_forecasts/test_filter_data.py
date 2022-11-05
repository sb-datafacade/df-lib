import pandas as pd

from applications.TimeSeriesForecast.code.ActionDefinition.FilteringData.python.ExecutionHandler import ExecutionHandler

def test_filter_data():
    df = pd.DataFrame({
        'A': {0: '1', 1: '2', 2: '2'},
        'B': {0: '2', 1: '1', 2: '1'}
    })

    handler = ExecutionHandler()
    final: pd.DataFrame = handler.execute(df, "A == '2' and B == '1'")

    assert final.to_json() == pd.DataFrame({
        'A': {1: '2', 2: '2'},
        'B': {1: '1', 2: '1'}}).to_json()
