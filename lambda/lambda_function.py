import boto3
import os

s3 = boto3.client("s3")

def lambda_handler(event, context):

    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]

    object_key = event["Records"][0]["s3"]["object"]["key"]

    metadata = s3.head_object(
        Bucket=bucket_name,
        Key=object_key
    )

    file_size = metadata["ContentLength"]

    upload_time = metadata["LastModified"]

    report = f"""
IMAGE METADATA REPORT

File Name: {object_key}

File Size (Bytes): {file_size}

Upload Time: {upload_time}
"""

    output_bucket = os.environ["OUTPUT_BUCKET"]

    output_file = f"{object_key}_metadata.txt"

    s3.put_object(
        Bucket=output_bucket,
        Key=output_file,
        Body=report
    )

    return {
        "statusCode": 200,
        "body": report
    }