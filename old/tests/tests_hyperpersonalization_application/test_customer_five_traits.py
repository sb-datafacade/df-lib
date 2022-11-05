import pandas as pd
from tests.helpers import load_data
from applications.HyperPersonalizationApplication.code.ActionDefinition.customer_five_personality_traits.python.ExecutionHandler import \
    ExecutionHandler


def test_customer_five_traits():
    execution_handler = ExecutionHandler()
    data = load_data("customer_segments.csv")
    psychographic_data = load_data("phyco_data.csv")
    segment_column = 'Segment'
    CustomerID = 'user'
    result = execution_handler.execute(data, CustomerID, psychographic_data, segment_column)
    expected_result = pd.DataFrame({"Segment": [0, 1, 2, 3], "Extroversion": ['Outgoing/Energetic', 'Neutral', 'Neutral', 'Neutral'],
                                    "Neuroticism": ['Resilient/Confident', 'Neutral', 'Resilient/Confident', 'Resilient/Confident'],
                                    'Agreeableness': ['Neutral', 'Friendly/Compassionate', 'Friendly/Compassionate', 'Friendly/Compassionate'],
                                    'Conscientiousness':['Efficient/Organized', 'Neutral', 'Efficient/Organized', 'Efficient/Organized'],
                                    'Openness': ['Inventive/Curious', 'Inventive/Curious', 'Inventive/Curious', 'Inventive/Curious']})
    pd.testing.assert_frame_equal(result, expected_result)