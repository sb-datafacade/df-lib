import pandas as pd
from applications.DataFacadeOOB.code.ActionDefinition.resample.python.ExecutionHandler import ExecutionHandler


def test_resample():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    d = {'price': [10, 11, 9, 13],
         'volume': [50, 60, 40, 100]}
    rng = ['01/01/2018', '01/09/2018', '01/05/2018', '01/03/2018']

    Data = pd.DataFrame(d, index=rng)
    frequency = 'Hourly'
    time_stamp_format = 'Infer'
    period = 24
    resample_method = 'Up-sample'
    result = execution_handler.execute(Data, frequency, time_stamp_format, period, resample_method)
    rng = pd.date_range('01/01/2018',
                        periods=9,
                        freq='24H')
    expected_result = pd.DataFrame({'price': [10, 10, 13, 13, 9, 9, 9, 9, 11],
                                    'volume': [50, 50, 100, 100, 40, 40, 40, 40, 60]}, index=rng)
    pd.testing.assert_frame_equal(result, expected_result)
    """
     -case2
    """
    d = {'price': [10, 11, 9, 13, 14, 18, 17, 19, 15],
         'volume': [50, 60, 40, 100, 50, 100, 40, 50, 50]}
    rng = pd.date_range('01/01/2018',
                        periods=9,
                        freq='W')

    Data = pd.DataFrame(d, index=rng)
    frequency = 'Month'
    time_stamp_format = 'Infer'
    period = 1
    resample_method = 'Down-sample'
    result = execution_handler.execute(Data, frequency, time_stamp_format, period, resample_method)
    rng = ['01/01/2018', '02/01/2018', '03/01/2018']
    rng = pd.to_datetime(rng, infer_datetime_format=True)
    expected_result = pd.DataFrame({'price': [10.75, 17, 15],
                                    'volume': [62.5, 60, 50]}, index=rng)
