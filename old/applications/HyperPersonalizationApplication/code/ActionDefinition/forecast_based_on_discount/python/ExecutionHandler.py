"""
Inputs:
    - data: Transformed data  in the form of dataframe
    - table_offer: Table consists of discount information
    - CustomerID: Unique id column to identify each customer
    - offer_id: Unique id column to identify each offer
    - discount_column: Columns consists of discount data
    -segment_column: Segment column
    - selected_segment: User selected segment
Output:
    - Table with recommended offers and discounts
"""
import pandas as pd
import numpy as np
from dft import df_plot
from dft.base_execution_handler import BaseExecutionHandler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.svm import SVC
import random


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, data, table_offer, demo_phy_data, discount_column, enrolment_column, subscription_column, gender_column, income_column, CustomerID, generate_forcast):
        try:
            table_offer.fillna(0, inplace=True)
            if sum(table_offer[discount_column] > 1) == 0:
                table_offer[discount_column] = table_offer[discount_column]*100
            else:
                pass
            if generate_forcast == 'Yes':
                unsubscribed_user = data['user']
                demo_phy_data[subscription_column] = table_offer[subscription_column]

                gender_sub_count = demo_phy_data.groupby(gender_column).agg({subscription_column: 'sum'}).reset_index()
                gender_sub_count[gender_column] = 'Gender:' + gender_sub_count[gender_column]
                gender_sub_count.rename(columns={gender_column: 'Category'}, inplace=True)

                demo_phy_data[income_column] = pd.qcut(demo_phy_data[income_column], q=[0, .25, .5, .75, 1.])
                demo_phy_data[income_column] = demo_phy_data[income_column]
                demo_phy_data.set_index(CustomerID, inplace=True)
                temp_df = demo_phy_data.loc[unsubscribed_user].reset_index()

                income_sub_count = demo_phy_data.groupby(income_column).agg(
                    {subscription_column: 'sum'}).reset_index().dropna()
                income_sub_count[income_column] = 'Income Group:' + income_sub_count[income_column].astype(str)
                income_sub_count.rename(columns={income_column: 'Category'}, inplace=True)

                sub_count = pd.concat([gender_sub_count, income_sub_count])
                # Offer Data Preparation
                X = table_offer[[discount_column, enrolment_column]].values
                y = table_offer[subscription_column].values

                clf = SVC(kernel='rbf', C=10, gamma=10)

                clf.fit(X, y)
                new_X = data[['Recommended_discount', enrolment_column]].values
                subscribed = clf.predict(new_X)
                temp_df.drop(subscription_column, axis=1, inplace=True)
                temp_df[subscription_column] = subscribed

                gender_sub_count_new = temp_df.groupby(gender_column).agg({subscription_column: 'sum'}).reset_index()
                gender_sub_count_new[gender_column] = 'Gender:' + gender_sub_count_new[gender_column]
                gender_sub_count_new.rename(columns={gender_column: 'Category'}, inplace=True)

                income_sub_count_new = temp_df.groupby(income_column).agg(
                    {subscription_column: 'sum'}).reset_index().dropna()
                income_sub_count_new[income_column] = 'Income Group:' + income_sub_count_new[income_column].astype(str)
                income_sub_count_new.rename(columns={income_column: 'Category'}, inplace=True)

                sub_count_new = pd.concat([gender_sub_count_new, income_sub_count_new]).round(1)
                sub_count['new_sub_count_%'] = (100 * sub_count_new[subscription_column]) / sub_count[
                    subscription_column]

                old_sub_count = table_offer[subscription_column].sum()
                new_sub_count = old_sub_count + subscribed.sum()
                inc = (new_sub_count - old_sub_count) / old_sub_count * 100
                if inc > 0:
                    s = 'Increment In Subscribed Users Is ' + str(inc.round(0)) + ' %'
                elif inc == 0:
                    s = 'No Change In Subscription Count'
                else:
                    s = 'Decrement In Subscribed Users Is ' + str(inc.round(0)) + ' %'
                print(s)
                p = str(new_sub_count) + ' (' + str(inc) + '%)'
                df_plot.single_value('Total Subscription Previous Month', old_sub_count)
                df_plot.single_value('Forecast For Next Month', new_sub_count)
                df_plot.single_value('Change In Subscription Count (in %)', inc.round(1))
                df_plot.bar_chart('Expected Number Conversion', 'Category', 'new_sub_count_%', sub_count)
            else:
                sub_count = 'Forecast Not Generated'

        except Exception as e:
            raise type(e)(e)

        return sub_count
