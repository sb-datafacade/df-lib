from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data):
        def drop_dup_row(df):
            df.drop_duplicates(keep='first', inplace=True)
        drop_dup_row(Data)
        return Data