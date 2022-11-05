import numpy as np
import pandas as pd
from tests.helpers import load_data
from applications.HyperPersonalizationApplication.code.ActionDefinition.fintech_customer_cohort_analysis.python.ExecutionHandler import \
    ExecutionHandler


def test_cohort_analysis():
    execution_handler = ExecutionHandler()
    fintech_data = load_data("fintech_data.csv")
    propensity_data = load_data("propensity_data.csv")
    CustomerID = 'user'
    result = execution_handler.execute(fintech_data, propensity_data, CustomerID).fillna(0).reset_index()
    expected_result = pd.DataFrame({'CohortIndex': range(0, 5),
                                    'index': pd.to_datetime(
                                        ['01/02/2013', '01/03/2013', '01/04/2013', '01/05/2013', '01/07/2013']),
                                    '1.0': [93.6, 0, 93.1, 91.3, 90],
                                    '2.0': [0, 88.1, 0, 84.7, 0],
                                    '3.0': [83.9, 0, 0, 0, 0]}).set_index('CohortIndex')
    np.array_equal(result.values, expected_result.values)
