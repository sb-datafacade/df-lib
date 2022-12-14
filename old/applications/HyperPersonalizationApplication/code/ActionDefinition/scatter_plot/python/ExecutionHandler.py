"""
Action for calculating first two principal component of the RFM table and add the value of those component to a new dataframe
Inputs:
    - segment_data: Dataframe with RFM values and segments
    - customer_id_column: Customer identification column of the segment_data
    - segment_column: Segment labels columns of segment_data
Output:
    - Modified Dataframe with RFM values and  the first two principal components values
"""""
import traceback
import pandas as pd
from dft import df_plot
from sklearn.preprocessing import StandardScaler
from dft.base_execution_handler import BaseExecutionHandler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import dirty_cat
import numpy as np


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, segment_data, customer_id_column, segment_column):

        from sklearn.decomposition import PCA
        try:
            pca = PCA(2)  # calculating the first two principal component
            data = segment_data.drop([customer_id_column, segment_column], axis=1)
            data = self.numeric_column_scale(data)
            data = self.categorical_column_encode(data)
            df = pca.fit_transform(data)
            PC1 = data.columns[pca.components_[0].argmax()] + " (Feature 1)"
            PC2 = data.columns[pca.components_[1].argmax()] + " (Feature 2)"
            d = pd.DataFrame(df)
            d[segment_column] = segment_data[segment_column]
            d.rename(columns={0: PC1, 1: PC2}, inplace=True)
            table = pd.pivot(d, values=PC2,
                             columns=segment_column).reset_index()
            n = len(d[segment_column].unique())
            table[PC1] = d[PC1]
            df_plot.multiple_series_scatter_chart('scatter plot', PC1, list(table.columns[1:n]), table)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            raise
        return table

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
