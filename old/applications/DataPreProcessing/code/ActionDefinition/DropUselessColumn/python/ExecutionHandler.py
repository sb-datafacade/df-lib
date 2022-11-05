from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,thres1):
        def drop(df):
            for col in df.columns:
                if df[col].isna().sum()/len(df[col])>thres1:
                   df.drop(col, inplace=True, axis=1)
        drop(Data)
        return Data