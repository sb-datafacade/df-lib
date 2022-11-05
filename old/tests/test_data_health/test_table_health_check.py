import json
import warnings

from applications.SystemApplication.code.ActionDefinition.TableAndColumnStats.python.ExecutionHandler import \
    ExecutionHandler
from tests.helpers import load_data


def test_table_health():
    warnings.filterwarnings('ignore')
    handler = ExecutionHandler()
    inp = load_data("salesforce_data_with_duplicates.csv")
    result = handler.execute(df=inp)
    assert result is not None
    res = json.loads(result)
    assert res["TableStat"]["Health"] <= 1.0

    inp = load_data("CohortDataSet.csv")
    result = handler.execute(df=inp)
    assert result is not None
    res = json.loads(result)
    assert res["TableStat"]["Health"] < 0.85
