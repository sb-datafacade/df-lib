import pandas as pd
from applications.STPModelApplication.code.ActionDefinition.convert_source_data_to_stp_model_schema.python.ExecutionHandler import \
    ExecutionHandler


def test_convert_stp_df():
    execution_handler = ExecutionHandler()
    Data = pd.DataFrame({"id": [0, 1], "name": ['jack', 'roy'], "date": ['10/12/2022', '12/08/2021'], "int_id": [0, 1]
                        , "value": [0, 1], "country": ['india', 'china'],
                         "comment": ['Hello world.', 'Python code.'],
                         "link": ['https://stage.datafacade.io/application', 'https://www.enginius.biz/'],
                         "lat": [-90.0, 45], 'long': [-127.554334, 180]})
    expected_result = pd.DataFrame(
        {"id": [0, 1], "name": ['jack', 'roy'], "int_id": [0, 1]
            , "value": [0, 1], "country": ['india', 'china']})
    result = execution_handler.execute(Data)
    pd.testing.assert_frame_equal(result, expected_result)
