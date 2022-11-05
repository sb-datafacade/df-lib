from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Data,thres1,thres2):
        def obj_impute(df,cols,thres2):
            for col in cols:
                if len(df[col].unique())/len(df[col])>thres2:
                   row=df[col].isna()
                   row=np.where(row)[0]
                   row=row.tolist()
                   df.drop(row,axis=0)
                elif len(df[col].unique())/len(df[col])<=thres2:
                     df[col].fillna(df[col].value_counts().index[0],inplace=True)
        df=Data
        df_object=list(df.select_dtypes(include=['object']).columns)
        df_object_na=df[df_object].columns[df[df_object].isnull().any()].tolist() 
        obj_impute(df, df_object_na,thres2)
        return df