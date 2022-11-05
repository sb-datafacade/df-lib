from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,thres1,thres2):
        def alpnum_tag(df,cols,thres2):
            alp=[]
            n=df.shape[0]
            for col in cols:
                if df[col].str.isalnum().sum()/n>thres2:
                   alp.append(col)
            return alp
        df=Data
        df_object=list(df.select_dtypes(include=['object']).columns)
        alphanum_tag=alpnum_tag(df,df_object,thres2)
        return pd.DataFrame(alphanum_tag,columns =['Column Names'])