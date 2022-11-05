import pandas as pd
from applications.TimeSeriesForecast.code.ActionDefinition.SampleData.python.ExecutionHandler import ExecutionHandler


def test_resample():
    execution_handler = ExecutionHandler()
    """
    -case1
    """
    d = {'price': [10, 11, 9, 13, 14, 18, 17, 19, 15],
         'volume': [50, 60, 40, 100, 50, 100, 40, 50, 50]}
    rng = ['01/10/2018', '31/01/2018', '01/02/2018', '01/05/2018',
           '05/09/2018', '02/03/2018', '01/01/2018', '01/11/2018', '01/06/2018']

    Data = pd.DataFrame(d, index=rng)
    frequency = 'Hourly'
    time_stamp_format = 'Infer'
    period = 10
    resample_method = 'Up-sample'
    result = execution_handler.execute(Data, frequency, time_stamp_format, period, resample_method)
    print(result)

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
    print(result)
