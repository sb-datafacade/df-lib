import pandas as pd

from applications.DataFacadeOOB.code.ActionDefinition.ColumnDistinctValues.python.ExecutionHandler import ExecutionHandler

def test_column_distinct_values():
    handler = ExecutionHandler()
    df = pd.DataFrame({
        'x': [1,2,3,3,4]
    })

    response = handler.execute(df, 'x')

    assert response == {
        'DistinctValues': [1,2,3,4]
    }