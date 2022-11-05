from applications.DataFacadeOOB.code.ActionDefinition.analyze_trends.python.ExecutionHandler import ExecutionHandler

from tests.helpers import load_data


def test_analyze_trends():
    handler = ExecutionHandler()
    inp = load_data("iris.csv")
    result = handler.execute(data=inp, dim_columns=["species"], target_col="sepal_length", agg_function="sum")
    assert result is not None
