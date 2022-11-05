import pandas as pd
from applications.RFM_Model_Application.code.ActionDefinition.convert_source_data_to_model_schema.python.ExecutionHandler import \
    ExecutionHandler


def test_df():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id": [0, 1], "name": ['jack', 'roy'], "date": ['10/12/2022', '12/08/2021'], "int_id": [0, 1], "value": [0, 1]})
    CustomerID = ['id', 'name']
    Interaction_ID = 'int_id'
    Interaction_Date = 'date'
    Interaction_Value = 'value'
    expected_result = pd.DataFrame(
        {"id": [0, 1], "name": ['jack', 'roy'], "ts_interaction": ['10/12/2022', '12/08/2021'], "n_interaction_value": [0.0, 1],
         "id_interaction": [0, 1]})
    result = execution_handler.execute(Data, CustomerID, Interaction_ID, Interaction_Date, Interaction_Value)
    pd.testing.assert_frame_equal(result, expected_result)
