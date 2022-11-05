from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,alphanum_tag,thres1,thres2):
        def alpnum_impute(df,cols,thres2):
            for col in cols:
                if len(df[col].unique())/len(df[col])>thres2:
                   r=df[col].str.isalnum()
                   r=[not elem for elem in r]
                   r=np.where(r)[0]
                   r=r.tolist()
                   df.drop(r,axis=0)
             elif len(df[col].unique())/len(df[col])<=thres2:
                  r=df[col].str.isalnum()
                  r=[not elem for elem in r]
                  df[col].loc[r]=df[col].value_counts().index[0]
        df=Data
        alpnum_impute(df, alphanum_tag,thres2)
        return df