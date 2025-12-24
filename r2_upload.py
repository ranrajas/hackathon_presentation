import boto3
import os

R2_ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
R2_ACCESS_KEY = os.environ["R2_ACCESS_KEY_ID"]
R2_SECRET_KEY = os.environ["R2_SECRET_ACCESS_KEY"]
R2_BUCKET = os.environ["R2_BUCKET_NAME"]
R2_PUBLIC_URL = os.environ["R2_PUBLIC_URL"]

s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=R2_ACCESS_KEY,
    aws_secret_access_key=R2_SECRET_KEY,
    region_name="auto"
)

def upload_to_r2(file_path, object_name):
    s3.upload_file(
        file_path,
        R2_BUCKET,
        object_name,
        ExtraArgs={
            "ContentType": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        }
    )

    return f"{R2_PUBLIC_URL}/{object_name}"
