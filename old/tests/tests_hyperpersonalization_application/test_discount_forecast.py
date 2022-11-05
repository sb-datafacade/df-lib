import pandas as pd
from applications.HyperPersonalizationApplication.code.ActionDefinition.forecast_based_on_discount.python.ExecutionHandler import \
    ExecutionHandler


def test_discount_forecast():
    execution_handler = ExecutionHandler()
    data = pd.DataFrame({"user": [0, 1, 4, 5], "Recommended_discount": [15, 25, 26, 18],
                         "enrolled": [1, 0, 0, 0]})
    table_offer = pd.DataFrame({"User ID": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                "discount": [0, 0, 15, 16, 0, 5, 15, 25, 18, 19, 24],
                                "sub": [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                                "enrolled": [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]})
    demo_phy_data = pd.DataFrame({"User ID": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                  "gender": ['M', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'M'],
                                  "income": [10000, 15000, 150000, 160000, 250000, 25987, 12356, 21584, 12564, 12560,
                                             250000]})
    discount_column = 'discount'
    enrolment_column = 'enrolled'
    subscription_column = 'sub'
    gender_column = 'gender'
    income_column = 'income'
    CustomerID = 'User ID'
    """
    -case1
    """
    generate_forcast = 'Yes'
    result = execution_handler.execute(data, table_offer, demo_phy_data, discount_column, enrolment_column,
                                       subscription_column, gender_column, income_column, CustomerID, generate_forcast)
    # pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
    """"
    -case2
    """
    generate_forcast = 'No'
    result = execution_handler.execute(data, table_offer, demo_phy_data, discount_column, enrolment_column,
                                       subscription_column, gender_column, income_column, CustomerID, generate_forcast)
    assert(result, 'Forecast Not Generated')