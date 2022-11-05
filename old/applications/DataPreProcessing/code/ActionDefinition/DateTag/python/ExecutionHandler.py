from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,thres1,thres2):
        def dt_tag(df,cols,thres2):
            date=[]
            n=df.shape[0]
            for col in cols:
                if pd.to_datetime(df[col], errors='coerce').notnull().sum()/n>thres2:
                   date.append(col)
            return date
        df=Data
        df_object=list(df.select_dtypes(include=['object']).columns)
        date_tag=dt_tag(df, df_object,thres2)
        return pd.DataFrame(date_tag,columns =['Column Names'])