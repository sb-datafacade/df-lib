from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,thres1,thres2):
        def num_impute(df,cols,thres2):
            for col in cols:
                if len(df[col].unique())/len(df[col])>thres2:
                   df[col].fillna(df[col].mean(),inplace=True)
                elif len(df[col].unique())/len(df[col])<=thres2:
                     df[col].fillna(df[col].mode()[0],inplace=True)
        df=Data
        df_numeric =list(df.select_dtypes(include=['int64','float64','bool']).columns)
        df_numeric_na=df[df_numeric].columns[df[df_numeric].isnull().any()].tolist()
        num_impute(df,df_numeric_na,thres2)
        return df