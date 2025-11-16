# def extract():
#     print('task is extracted')


import boto3
import pandas as pd
import os
from io import StringIO

def extract(**kwargs):
    # S3 credentials (⚠️ Production me Airflow Connections me rakho)
    ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID") 
    SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY") 
    BUCKET_NAME = "cubeq42024"
    OBJECT_KEY = "model list/model list.csv"  # s3 path inside bucket

    # Create boto3 client
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=os.getenv("AWS_DEFAULT_REGION")
    )

    # Download file into memory
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
    file_content = response["Body"].read().decode("utf-8")

    # Convert CSV into pandas DataFrame
    df = pd.read_csv(StringIO(file_content))

    # Push DataFrame to XCom for transform step
    ti = kwargs["ti"]
    ti.xcom_push(key="raw_data", value=df.to_dict())

    print("✅ Extracted data from S3:", df.head())
    return "extract completed"
