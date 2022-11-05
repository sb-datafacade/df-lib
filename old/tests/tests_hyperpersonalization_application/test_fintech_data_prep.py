import pandas as pd
from tests.helpers import load_data
from applications.HyperPersonalizationApplication.code.ActionDefinition.fintech_data_preparation.python.ExecutionHandler import \
    ExecutionHandler


def test_fintech_data_prep():
    execution_handler = ExecutionHandler()
    Data = load_data("fintech_data.csv")
    result = execution_handler.execute(Data)
    table = Data
    table['response_time'] = (table.enrolled_date - table.first_open).astype('timedelta64[h]')
    table = table.drop(columns=['enrolled_date', 'response_time', 'first_open'])
    pd.testing.assert_frame_equal(result, table)
