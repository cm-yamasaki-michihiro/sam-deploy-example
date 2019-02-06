import json

import requests

import boto3


def create_bucket(s3, bucket_name):
    s3.create_bucket(Bucket=bucket_name)


def lambda_handler(event, context):
    client = boto3.client('s3')
    create_bucket(client, "fuga")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "hello world", "location": ip.text.replace("\n", "")}
        )
    }
