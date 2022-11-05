import json
import traceback

import numpy as np
import re
import time
import timeit
import datetime


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return super().encode(bool(obj))
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return super(NpEncoder, self).default(obj)


# TODO: Move it to dft or use profiler.
def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        execution_time = (time2 - time1)
        if execution_time > 0.1:
            print('`{:s}` function took {:.3f} sec'.format(f.__name__, execution_time))

        return ret

    return wrap


from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def __init__(self):
        self.column_healths = []
        self.int_columns = 0
        self.float_columns = 0
        self.bool_columns = 0
        self.object_columns = 0

    @timing
    def execute(self, df):
        stats = {
            "ColumnInfoAndStats": self.form_column_info_and_stats(df),
            "TableStat": self.form_table_stat(df)
        }

        json_string = json.dumps(stats, indent=4, cls=NpEncoder)
        print(json_string)
        return json_string

    def form_table_stat(self, df, w1=0.7):

        return {
            "RowCount": len(df.index),
            "IntColumnCount": self.int_columns,
            "FloatColumnCount": self.float_columns,
            "BoolColumnCount": self.bool_columns,
            "StringColumnCount": self.object_columns,
            "DuplicateRowCount": df.duplicated().sum(),
            "Health": 0 if len(self.column_healths) == 0 else 1 - w1 * (
                    1 - sum(self.column_healths) / len(self.column_healths)) - (1 - w1) * (
                                                                      df.duplicated().sum() / df.shape[0])
        }

    def form_column_info_and_stats(self, df):
        col_info = []
        for col_name in df.columns:
            col_info.append({
                "ColumnName": col_name,
                "ColumnStat": self.form_stat_for_column(df, col_name)
            })
        return col_info

    def form_stat_for_column(self, df, col):
        try:
            if "float" in str(df[col].dtype):
                self.float_columns += 1
                return self.form_stat_for_float_column(df, col)
            elif "int" in str(df[col].dtype):
                self.int_columns += 1
                return self.form_stat_for_int_column(df, col)
            elif "bool" in str(df[col].dtype):
                self.bool_columns += 1
                return self.form_stat_for_bool_column(df, col)
            elif "object" in str(df[col].dtype):
                self.object_columns += 1
                return self.form_stat_for_object_column(df, col)
            else:
                return {
                    "ColumnDatatype": "NA"
                }
        except Exception as e:
            print(f"Exception occurred to compute stat for {col}")
            print(e)
            print(traceback.format_exc())
            return {
                "ColumnDatatype": df[col].dtype,
                "Health": 0
            }

    def form_stat_for_float_column(self, df, col):
        stat = {
            "ColumnDatatype": "Float",
            "Validity": self.form_validity_stat(df, col),
            "ContentStat": self.form_content_stat(df, col),

            "MeanModeStDev": self.form_mean_mode_st_dev_stat(df, col),
            "QuartileStat": self.form_quartile_stat(df, col),
            "Outlier": self.form_outlier_stat(df, col),
            "Correlation": self.form_correlation_stat(df, col)
        }

        column_health = self.calculate_health_for_float_column(stat)
        self.column_healths.append(column_health)
        stat["Health"] = column_health
        return stat

    def form_stat_for_int_column(self, df, col):
        stat = {
            "ColumnDatatype": "Int",
            "Validity": self.form_validity_stat(df, col),
            "ContentStat": self.form_content_stat(df, col),

            "MeanModeStDev": self.form_mean_mode_st_dev_stat(df, col),
            "QuartileStat": self.form_quartile_stat(df, col),
            "Correlation": self.form_correlation_stat(df, col)
        }

        column_health = self.calculate_health_for_int_column(stat)
        self.column_healths.append(column_health)
        stat["Health"] = column_health
        return stat

    def form_stat_for_bool_column(self, df, col):
        stat = {
            "ColumnDatatype": "Boolean",
            "Validity": self.form_validity_stat(df, col),
            "ContentStat": self.form_content_stat(df, col),
            "Correlation": self.form_correlation_stat(df, col)
        }

        column_health = self.calculate_health_for_bool_column(stat)
        self.column_healths.append(column_health)
        stat["Health"] = column_health
        return stat

    def form_stat_for_object_column(self, df, col):
        stat = {
            "ColumnDatatype": "String",
            "Validity": self.form_validity_stat(df, col),
            "ContentStat": self.form_content_stat(df, col),
            "Correlation": self.form_correlation_stat(df, col),
            "MostFrequent": self.form_most_frequent_stat(df, col)
        }

        column_health = self.calculate_health_for_object_column(stat)
        self.column_healths.append(column_health)
        stat["Health"] = column_health
        return stat

    def calculate_health_for_float_column(self, stat, w1=0.5, w2=0.3):
        non_empty_rows = stat["Validity"]["ValidRowCount"]
        empty_rows = stat["Validity"]["EmptyRowCount"]
        outlier_rows_count = stat["Outlier"]["OutlierRowCount"]
        correlation = stat["Correlation"]["CorrelationStat"]
        total_rows = non_empty_rows + empty_rows

        if total_rows == 0:
            return 0

        healths = [
            1 - w1 * (empty_rows / total_rows) - w2 * (outlier_rows_count / total_rows) - (1 - w1 - w2) * correlation
        ]

        return sum(healths) / len(healths)

    def calculate_health_for_int_column(self, stat, w1=0.5):
        non_empty_rows = stat["Validity"]["ValidRowCount"]
        empty_rows = stat["Validity"]["EmptyRowCount"]
        correlation = stat["Correlation"]["CorrelationStat"]
        total_rows = non_empty_rows + empty_rows

        if total_rows == 0:
            return 0

        healths = [
            1 - w1 * (empty_rows / total_rows) - (1 - w1) * correlation
        ]

        return sum(healths) / len(healths)

    def calculate_health_for_bool_column(self, stat, w1=0.7):
        non_empty_rows = stat["Validity"]["ValidRowCount"]
        empty_rows = stat["Validity"]["EmptyRowCount"]
        correlation = stat["Correlation"]["CorrelationStat"]
        total_rows = non_empty_rows + empty_rows

        if total_rows == 0:
            return 0

        healths = [
            1 - w1 * (empty_rows / total_rows) - (1 - w1) * correlation
        ]

        return sum(healths) / len(healths)

    def calculate_health_for_object_column(self, stat, w1=0.5, w2=0.3):
        non_empty_rows = stat["Validity"]["ValidRowCount"]
        empty_rows = stat["Validity"]["EmptyRowCount"]
        invalid_rows = stat["Validity"]["InValidRowCount"]
        correlation = stat["Correlation"]["CorrelationStat"]
        total_rows = non_empty_rows + empty_rows + invalid_rows

        if total_rows == 0:
            return 0

        healths = [
            1 - w1 * (empty_rows / total_rows) - w2 * (invalid_rows / total_rows) - (1 - w1 - w2) * correlation
        ]

        return sum(healths) / len(healths)

    @timing
    def form_validity_stat(self, df, col):
        invalid_count = self.form_consistency_stat(df, col)
        return {
            "ValidRowCount": len(df.index) - df[col].isna().sum() - invalid_count,
            "InValidRowCount": invalid_count,
            "EmptyRowCount": df[col].isna().sum()
        }

    @timing
    def form_outlier_stat(self, df, col, times=1.5):
        # Here we are use 5 standard deviation limit from mean to detect outliers
        # TODO: Disabling it due to high execution time. Suggest to move it to separate action
        # outlier_count = df[col].apply(
        #     lambda x: x - df[col].quantile(0.25) < -times * (df[col].quantile(0.75) - df[col].quantile(0.25))
        #               or x - df[col].quantile(0.75) > times * (df[col].quantile(0.75) - df[col].quantile(0.25))).sum()
        return {
            "OutlierRowCount": 0
        }

    @timing
    def form_mean_mode_st_dev_stat(self, df, col):
        mean = df[col].mean()
        mode = df[col].mode()
        if mode is not None and mode.iloc.obj.size > 0:
            mode = mode.iloc[0]
        else:
            mode = None
        stdDev = df[col].std()
        return {
            "Mean": mean,
            "Mode": mode,
            "StDev": stdDev
        }

    @timing
    def form_content_stat(self, df, col):
        mode = None if len(df[col].mode()) == 0 else df[col].mode().iloc[0]
        return {
            "UniqueValues": df[col].nunique(),
            "MostCommonValue": mode,
            "MostCommonValueCount": (df[col] == mode).sum(),
            "TotalValues": df[col].count()
        }

    @timing
    def form_quartile_stat(self, df, col):
        return {
            "Minimum": df[col].min(),
            "Q1": df[col].quantile(0.25),
            "Median": df[col].median(),
            "Q3": df[col].quantile(0.75),
            "Maximum": df[col].max()
        }

    @timing
    def form_correlation_stat(self, df, col):
        # TODO: Disabling correlation stat as it's taking a lot of time
        # correlation_stat = self.calculate_correlation(col, df)
        correlation_stat = 0
        return {
            "CorrelationStat": correlation_stat
        }

    def calculate_correlation(self, col, df):
        if "float" in str(df[col].dtype) or "int" in str(df[col].dtype):
            correlation = []
            columns = df.select_dtypes(include=['int', 'float']).columns
            columns = columns.drop(col)
            if len(columns) > 0:
                for column in columns:
                    cor = df[column].corr(df[col])
                    correlation.append(cor)
                if max(correlation) >= 0.95:
                    correlation_stat = max(correlation)
                else:
                    correlation_stat = 0
            else:
                correlation_stat = 0

        elif "object" in str(df[col].dtype) or "bool" in str(df[col].dtype):
            correlation_stat = 0
            columns = df.select_dtypes(include=['object', 'bool']).columns
            columns = columns.drop(col)
            if len(columns) > 0:
                for column in columns:
                    df1 = df[[column, col]].T
                    correlated = df1.duplicated().max()
                    if correlated:
                        correlation_stat = 1
                        break
            else:
                correlation_stat = 0
        return correlation_stat

    @timing
    def form_most_frequent_stat(self, df, col):
        try:
            most_frequent_n = 5
            most_frequent_dict = df[col].value_counts().nlargest(most_frequent_n).to_dict()
            element_with_count = []
            for element in most_frequent_dict:
                frequency = most_frequent_dict[element]
                element_with_count.append({
                    "Element": element,
                    "Frequency": frequency
                })
        except Exception as e:
            print(e)
            print(traceback.format_exc())

        if len(element_with_count) == 0:
            element_with_count.append({
                "Element": "",
                "Frequency": 0
            })

        return {
            "ElementWithCount": element_with_count
        }

    @timing
    def form_consistency_stat(df, col, threshold_percentage=0.6):

        def float_check(element):
            if re.match(r"^-?\d+(?:\.\d+)$", element) is not None:
                return True
            else:
                return False

        invalid = 0

        try:
            if "object" in str(df[col].dtype):
                if df[col].str.isnumeric().sum() / len(df[col].dropna()) > threshold_percentage:
                    invalid = len(df[col].dropna()) - df[col].str.isnumeric().sum()

                elif (sum(df[col].dropna().map(lambda x: float_check(x))) + df[col].str.isnumeric().sum()) / len(
                        df[col].dropna()) > threshold_percentage:
                    invalid = len(df[col].dropna()) - sum(df[col].dropna().map(lambda x: float_check(x))) - df[
                        col].str.isnumeric().sum()
            else:
                invalid = 0

        except Exception as e:
            invalid = 0

        return invalid
