import pandas as pd
from tests.helpers import load_data
from applications.HyperPersonalizationApplication.code.ActionDefinition.demographic_data_preparation.python.ExecutionHandler import \
    ExecutionHandler


def test_demographics_data_prep():
    execution_handler = ExecutionHandler()
    Data = load_data("demographics.csv")
    result = execution_handler.execute(Data)
    table = Data
    table = table.drop(columns=['DisbursalDate', 'MaturityDate', 'AuthDate', 'LTV', 'ZipCODE',
                                'AssetCost', 'AmountFinance', 'DisbursalAmount', 'EMI'])
    pd.testing.assert_frame_equal(result, table)
