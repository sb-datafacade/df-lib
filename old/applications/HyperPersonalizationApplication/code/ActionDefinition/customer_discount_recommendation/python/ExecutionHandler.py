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
from sklearn.cluster import KMeans
import dirty_cat
import random


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, data, table_offer, propensity_data, CustomerID, offer_id, discount_column, segment_column, selected_segment, segment_data, subscription_column, propensity_column, lower_range_discount, upper_range_discount):
        try:

            # Offer Data Preparation
            if sum(table_offer[discount_column] > 1) == 0:
                table_offer[discount_column] = table_offer[discount_column]*100
            else:
                pass
            print('Offer Data Preparation Done')
            df_discounts = table_offer[['user', offer_id, discount_column]].copy()
            df_discounts[discount_column] = df_discounts[discount_column].apply(
                lambda x: upper_range_discount if x > upper_range_discount else (
                    lower_range_discount if x < lower_range_discount else x))

            # Clustering
            print('Clustering Starts')
            df = data.copy()
            df.drop(CustomerID, axis=1, inplace=True)
            df = self.numeric_column_scale(df)
            df = self.categorical_column_encode(df)
            subscribed_user = table_offer[subscription_column] == 1
            unsubscribed_user = segment_data.index[segment_data[segment_column] == selected_segment].tolist()
            subscribed_user_data = df[subscribed_user]

            segment_data.set_index(segment_column, inplace=True)
            segment_data = segment_data.loc[selected_segment].reset_index()
            unsubscribed_user = segment_data[CustomerID]
            df[CustomerID] = data[CustomerID]
            df.set_index(CustomerID, inplace=True)
            unsubscribed_user_data = df.loc[unsubscribed_user]

            df = df.reset_index().drop(CustomerID, axis=1)
            print('data transformation complete')
            X = subscribed_user_data.values
            n_clusters = 60
            model = KMeans(n_clusters=n_clusters, random_state=0, verbose=False)

            model.fit(X)
            clusters = model.labels_
            subscribed_user_data['Cluster'] = clusters
            predict_cluster = model.predict(unsubscribed_user_data)

            propensity_data.set_index('user', inplace=True)
            temp_df_2 = propensity_data.loc[unsubscribed_user].reset_index()
            propensity_data = propensity_data.reset_index()

            cluster = pd.DataFrame({'Cluster': predict_cluster})
            temp_df_2 = pd.concat([temp_df_2, cluster], axis=1).dropna()
            temp_df_2[CustomerID] = unsubscribed_user

            # discount prediction
            df_discounts = df_discounts[subscribed_user]
            df_discounts['Cluster'] = subscribed_user_data['Cluster']

            def discount_reco(user_id, df_2):

                i = df_2[df_2[CustomerID] == user_id]['Cluster'].values[0]
                propensity = df_2[df_2[CustomerID] == user_id][propensity_column].values[0]
                temp_df = df_discounts[df_discounts['Cluster'] == i]
                unique_discounts = temp_df[discount_column].unique()
                if len(unique_discounts) > 1:
                    disc_freq = temp_df[discount_column].value_counts()
                    for j in range(1, len(unique_discounts) + 1):
                        if propensity <= df_2[propensity_column].quantile(j / len(unique_discounts)):
                            discount = disc_freq.reset_index()['index'][j-1]
                        else:
                            pass
                else:
                    discount = temp_df[discount_column].unique()[0]

                return discount

            temp_df_copy = temp_df_2.copy()
            temp_df_2['Recommended_discount'] = temp_df_2[CustomerID].map(lambda x: discount_reco(x, temp_df_copy))
            temp_df_2.drop([CustomerID], axis=1, inplace=True)
            table = pd.DataFrame(temp_df_2['Recommended_discount'].value_counts()).reset_index()
            table.columns = ['Discount', 'Count']
            table = table.sort_values(by=['Discount'])
            df_plot.line_chart('Discount Distribution', 'Discount', 'Count', table)

        except Exception as e:
            raise type(e)(e)

        return temp_df_2

    def categorical_column_encode(self, data: pd.DataFrame):
        columns = list(data.select_dtypes(include=['object']).columns)
        distinct_values = dict(map(lambda x: (x, len(pd.unique(data[x]))), columns))
        least_distinct_columns = list(dict(filter(lambda x: x[1] <= 5, distinct_values.items())).keys())
        mid_distinct_columns = list(dict(filter(lambda x: 5 < x[1] <= 10, distinct_values.items())).keys())
        most_distinct_values = list(dict(filter(lambda x: 10 < x[1], distinct_values.items())).keys())

        if len(least_distinct_columns):
            data = self.one_hot_encode(data, least_distinct_columns, drop_columns=True)
        if len(mid_distinct_columns):
            data = self.original_encode(data, mid_distinct_columns)
        if len(most_distinct_values):
            data = self.similarity_encode(data, most_distinct_values)

        return data

    def one_hot_encode(self, data: pd.DataFrame, columns, drop_columns):
        try:
            encoder = OneHotEncoder(sparse=False, handle_unknown='ignore').fit(data[columns])

            encoded_cols = list(encoder.get_feature_names_out(columns))

            data[encoded_cols] = encoder.transform(data[columns])
            if drop_columns:
                data = data.drop(columns, axis=1)

            for col in columns:
                print(col + " is " + "encoded")
            return data

        except Exception as e:
            raise type(e)(e)

    def original_encode(self, data: pd.DataFrame, columns):
        try:
            encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=np.nan).fit(data[columns])
            new_names = [column + '_' + 'encode' for column in columns]
            data[new_names] = pd.DataFrame(encoder.transform(data[columns]))
            data.drop(columns, axis=1, inplace=True)
            for col in columns:
                print(col + " is " + "encoded")
            return data
        except Exception as e:
            raise type(e)(e)

    def similarity_encode(self, data: pd.DataFrame, columns):
        try:
            for col in columns:
                encoder = dirty_cat.SimilarityEncoder(similarity='ngram')
                encoded_df = pd.DataFrame(encoder.fit_transform(data[[col]]))
                encoded_df.columns = [col + '_' + str(i) for i in encoded_df.columns]
                data = pd.concat([data, encoded_df], axis=1)
                data.drop(col, axis=1, inplace=True)
                print(col + " is " + "encoded")

            return data
        except Exception as e:
            raise type(e)(e)

    def numeric_column_scale(self, data: pd.DataFrame):
        from sklearn.preprocessing import MinMaxScaler
        columns = list(data.select_dtypes(include=['int', 'float']).columns)
        for col in columns:
            if data[col].dtype == 'float':
                scaler = MinMaxScaler().fit(data[[col]])
                data[col] = scaler.transform(data[[col]])

                print(col + ' Is Normalized')
            else:
                if data[col].nunique() / len(data[col]) > 0.5:
                    scaler = MinMaxScaler().fit(data[[col]])
                    data[col] = scaler.transform(data[[col]]).round(2)
                    print(col + ' Is Normalized')
                else:
                    dummies = pd.get_dummies(data[col])
                    dummies.columns = [col + '_' + str(i) for i in list(dummies.columns)]
                    data = pd.concat([data, dummies], axis=1)
                    data = data.drop(col, axis=1)
                    print(col + ' Is Normalized')

        return data
