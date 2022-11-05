from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def __init__(self):
        self.session = boto3.Session(aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name =aws_region)
        self.client = self.session.client("sagemaker")

    def execute(self, Table, Model):
        prepared_df = self.preprocess_data(Table, Model)
        prediction_handler = PredictionHandler(self.session, prepared_df, Model["OutputArtifact"], Model["Framework"])
        prediction = prediction_handler.get_prediction()
        return prediction

    def preprocess_data(self, table, model):
        target_column=model["Config"]["TargetColumn"]
        all_columns = table.columns.tolist()

        if target_column in all_columns:
            all_columns.remove(target_column)

        all_columns.sort()
        output_df = table[all_columns]

        return output_df