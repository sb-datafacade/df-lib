import datetime
import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.rfm_calculation.python.ExecutionHandler import \
    ExecutionHandler


def test_rfm_calculation():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id_customer": [0, 1], "name": ['jack', 'roy'], "phone": ['12121', '12121'],
                         "ts_interaction": pd.to_datetime(['10/12/2020', '12/08/2021'])
                        , "n_interaction_value": [100, 200], "id_interaction": [2222, 1111]})
    rfm_data = Data
    id_customer = ["id_customer", "name", "phone"]
    ts_interaction = "ts_interaction"
    id_interaction = "id_interaction"
    n_interaction_value = "n_interaction_value"
    result = execution_handler.execute(rfm_data, id_customer, ts_interaction, id_interaction, n_interaction_value)
    today_date = pd.to_datetime(datetime.date.today())
    recency = (today_date - Data['ts_interaction']).map(lambda x: x.days)
    t = (today_date - Data['ts_interaction']).map(lambda x: x.days)
    expected_result = pd.DataFrame({"id_customer": [0, 1], "name": ['jack', 'roy'], "phone": ['12121', '12121'],
                                    "Recency": recency, "T": t
                                    , "Frequency": [1, 1], "Monetary.min": [100, 200], "Monetary.avg": [100.0, 200.0]
                                    , "Monetary.max": [100, 200], "Monetary": [100.0, 200.0]})
    pd.testing.assert_frame_equal(result, expected_result, check_dtype=False)
