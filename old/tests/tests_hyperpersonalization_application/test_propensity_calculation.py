import pandas as pd
from tests.helpers import load_data
from applications.HyperPersonalizationApplication.code.ActionDefinition.propensity_calculation_cohort_building.python.ExecutionHandler import \
    ExecutionHandler


def test_propensity_calculation():
    execution_handler = ExecutionHandler()
    source_data = load_data("fintech_data.csv")
    transformed_data = load_data("propensity_data.csv").drop('Propensity', axis=1)[0:4]
    target_column = 'enrolled'
    discount_id_column = 'discount'
    discount_column = 'offer_id'
    subscription_column = 'subscribed'
    CustomerID = 'user'
    propensity_lower_limit = 0
    propensity_upper_limit = 100
    """
    -case1
    """
    method = 'Logistic Regression'
    result = execution_handler.execute(source_data, transformed_data, target_column, subscription_column,
                                       discount_id_column, discount_column,
                                       CustomerID, propensity_lower_limit, propensity_upper_limit, method).round(1)
    table = load_data("fintech_data.csv")[0:4]
    table['Propensity'] = [81.8, 17.9, 82.9, 17.4]
    pd.testing.assert_frame_equal(result, table, check_dtype=False)

    """
    -case2
    """
    method = 'Decision Tree Classifier'
    result = execution_handler.execute(source_data, transformed_data, target_column, subscription_column,
                                       discount_id_column, discount_column,
                                       CustomerID, propensity_lower_limit, propensity_upper_limit, method).round(1)
    table = load_data("fintech_data.csv")[0:4]
    table['Propensity'] = [100, 0, 100, 0]
    pd.testing.assert_frame_equal(result, table, check_dtype=False)

    """
    -case3
    """
    method = 'Random Forest Classifier'
    result = execution_handler.execute(source_data, transformed_data, target_column, subscription_column,
                                       discount_id_column, discount_column,
                                       CustomerID, propensity_lower_limit, propensity_upper_limit, method).round(1)
    table = load_data("fintech_data.csv")[0:4]
    table['Propensity'] = [80.0, 29.0, 79.0, 20.0]
    pd.testing.assert_frame_equal(result, table, check_dtype=False)

    """
    -case4
    """
    method = 'XGBoost Classifier'
    result = execution_handler.execute(source_data, transformed_data, target_column, subscription_column,
                                       discount_id_column, discount_column,
                                       CustomerID, propensity_lower_limit, propensity_upper_limit, method).round(1)
    table = load_data("fintech_data.csv")[0:4]
    table['Propensity'] = [50, 50, 50, 50]
    pd.testing.assert_frame_equal(result, table, check_dtype=False)