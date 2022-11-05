import json


from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def __init__(self):
        self.session = boto3.Session(aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name =aws_region)
        self.client = self.session.client("sagemaker")

    def execute(self, ModelName, num_round, predictor_type, Table, ModelURI):
        TargetColumn = Table.columns.tolist()[0]
        # Prepare Cleaned CSV from Dataframe and Upload to S3
        prepared_df = self.preprocess_data(Table, TargetColumn)
        prepared_csv_for_s3_upload = self.df_to_csv(prepared_df)
        file_name = get_random_string(20)
        s3_file_path = form_s3_path(form_file_path_for_cleaned_file(file_name))
        upload_to_s3(prepared_csv_for_s3_upload, s3_file_path)

        print("Train Job: Start")
        # Train Model on Sagemaker
        hyperparameters = self.form_hyperparameters(num_round, predictor_type)
        aws_response = self.train_model(ModelName, ModelURI, hyperparameters, form_s3_url(s3_file_path))
        print("Train Job: End")

        print("Wait for Train Job to Complete: Start")
        # Wait for Training to complete
        self.wait_for_training_job_to_complete(ModelName)
        print("Wait for Train Job to Complete: End")

        print("Fetch Trained Param Loction: Start")
        # Fetch location of Trained Model Artifact
        model_artifact_location = self.get_model_artifact_location(ModelName)
        print(f"Fetch Trained Param Loction: End({model_artifact_location})")

        print("Create Model: Start")
        # Create Model from training job
        self.create_model(ModelName, ModelURI, model_artifact_location)
        print("Create Model: End")

        print("Create Endpoint Config: Start")
        # Create Endpoint Config
        self.create_endpoint_config(ModelName)
        print("Create Endpoint Config: End")

        print("Create Endpoint: Start")
        # Create Serverless Endpoint
        self.create_serverless_endpoint(ModelName)
        print("Create Endpoint: End")

        print("Wait for Endpoint: Start")
        # Wait for Serverless Endpoint to come online
        self.wait_for_serverless_endpoint_to_come_online(ModelName)
        print("Wait for Endpoint: End")

        # Delete Cleaned File
        delete_file_from_s3(s3_file_path)

        # Form response and return
        return self.form_response(aws_response, ModelName, TargetColumn, model_artifact_location)

    def get_model_artifact_location(self, model_name):
        aws_response = self.client.describe_training_job(
            TrainingJobName=self.form_training_job_name(model_name)
        )

        return aws_response["ModelArtifacts"]["S3ModelArtifacts"]

    def preprocess_data(self, table, target_column):
        all_columns = table.columns.tolist()
    #     print("Columns In Dataframe  : ", all_columns)

        all_columns.remove(target_column)
    #     print("Columns Without Target: ", all_columns)

        all_columns.sort()
    #     print("Feature Column Order  : ", all_columns)

        column_order = [target_column] + all_columns
    #     print("All Column Final Order: ", column_order)

        output_df = table[column_order]
        return output_df

    def df_to_csv(self, df):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, header=False, index=False)
        return csv_buffer

    def form_hyperparameters(self, num_round, predictor_type):
        return {
            "num_round": str(num_round)
        }

    def train_model(self, model_name, model_uri, hyperparameters, input_file_path):
        aws_response = self.client.create_training_job(
            TrainingJobName=self.form_training_job_name(model_name),
            HyperParameters=hyperparameters,
            AlgorithmSpecification={
                "TrainingImage": model_uri,
                "TrainingInputMode": "File",
            },
            RoleArn="arn:aws:iam::721453078612:role/service-role/AmazonSageMaker-ExecutionRole-20211117T192273",
            InputDataConfig=[
                {
                    "ChannelName": "train",
                    "DataSource": {
                        "S3DataSource": {
                            "S3DataType": "S3Prefix",
                            "S3Uri": input_file_path
                        }
                    },
                    "ContentType": "text/csv",
                }
            ],
            OutputDataConfig={
                "S3OutputPath": self.form_s3_output_path(model_name)
            },
            CheckpointConfig={
                "S3Uri": self.form_s3_checkpoint_path(model_name)
            },
            ResourceConfig={
                "InstanceType": "ml.c5.2xlarge",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10
            },
            StoppingCondition={
                "MaxRuntimeInSeconds": 1200
            }
        )

        return aws_response

    def wait_for_training_job_to_complete(self, model_name):
        while True:
            response = self.client.describe_training_job(
                TrainingJobName=self.form_training_job_name(model_name)
            )
            training_status = response["TrainingJobStatus"]
            secondary_training_status = response["SecondaryStatus"]

            if training_status == "InProgress":
                time.sleep(2)
            elif training_status == "Completed":
                return
            else:
                raise ValueError(f"Sagemaker Training Job in unexpected status: {training_status}")

    def form_response(self, aws_response, model_name, target_column, model_artifact_location):
        response = {
            "ModelName": model_name,
            "TrainingJobArn": aws_response["TrainingJobArn"],
            "TargetColumn": target_column,
            "Framework": "xgboost",
            "OutputArtifact": model_artifact_location
        }

        return pd.DataFrame([response])

    def create_model(self, model_name, model_uri, model_artifact_location):
         aws_response = self.client.create_model(
            ModelName=self.form_model_name(model_name),
            PrimaryContainer={
                "Image": model_uri,
                "Mode": "SingleModel",
                "ModelDataUrl": model_artifact_location
            },
            ExecutionRoleArn="arn:aws:iam::721453078612:role/service-role/AmazonSageMaker-ExecutionRole-20211117T192273"
         )
         return aws_response["ModelArn"]

    def create_endpoint_config(self, model_name):
        aws_response = self.client.create_endpoint_config(
            EndpointConfigName=self.form_endpoint_config_name(model_name),
            ProductionVariants= [
                {
                    'VariantName': self.form_production_variant_name(model_name),
                    'ModelName': self.form_model_name(model_name),
                    'ServerlessConfig': {
                        'MemorySizeInMB': 2048,
                        'MaxConcurrency': 2
                    }
                }
            ]
        )

        return aws_response["EndpointConfigArn"]

    def create_serverless_endpoint(self, model_name):
        aws_response = self.client.create_endpoint(
            EndpointName=self.form_endpoint_name(model_name),
            EndpointConfigName=self.form_endpoint_config_name(model_name)
        )

        return aws_response["EndpointArn"]

    def wait_for_serverless_endpoint_to_come_online(self, model_name):
        while True:
            aws_response = self.client.describe_endpoint(
                EndpointName=self.form_endpoint_name(model_name)
            )
            endpoint_status = aws_response["EndpointStatus"]
            print(endpoint_status)
            if endpoint_status == "Creating":
                time.sleep(2)
            elif endpoint_status == "Failed":
                failure_reason = aws_response['FailureReason']
                raise ValueError(f"Sagemaker Endpoint Deployment failed due to: {failure_reason}")
            elif endpoint_status == "InService":
                return
            else:
                raise ValueError(f"Sagemaker Endpoint Deployment in unexpected status: {endpoint_status}")

    def form_endpoint_name(self, model_name):
        return f"{model_name}-Endpoint"

    def form_production_variant_name(self, model_name):
        return f"{model_name}-Production-Variant"

    def form_endpoint_config_name(self, model_name):
        return f"{model_name}-Endpoint-Config"

    def form_model_name(self, model_name):
        return f"{model_name}-Model"

    def form_training_job_name(self, model_name):
        return f"{model_name}-Training-Job"

    def form_s3_output_path(self, model_name):
        return form_s3_url(form_s3_path(f"/models/sagemaker/{model_name}/output"))

    def form_s3_checkpoint_path(self, model_name):
        return form_s3_url(form_s3_path(f"/models/sagemaker/{model_name}/checkpoint"))
