from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,thres1,thres2):
        def num_garbage(df,cols,thres2):
            for col in cols:
                n=df.shape[0]
                r=pd.to_numeric(df[col], errors='coerce').notnull().sum()
                if r/n>thres2:
                   if len(df[col].unique())/len(df[col])>thres2:
                      df[col]=pd.to_numeric(df[col], errors='coerce')
                      df[col].fillna(df[col].mean(),inplace=True)
                      print('1')
                   elif len(df[col].unique())/len(df[col])<=thres2:
                        df[col]=pd.to_numeric(df[col], errors='coerce')
                        df[col].fillna(df[col].mode()[0],inplace=True)
            
        df=Data
        df_object=list(df.select_dtypes(include=['object']).columns)
        num_garbage(df, df_object,thres2)
        return df