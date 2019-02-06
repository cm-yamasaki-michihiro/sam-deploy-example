
import json
import boto3
import pytest
import os
from handlers import helloworld1


def test_lambda_handler():
    s3 = boto3.resource('s3', endpoint_url='http://localhost:4572')
    helloworld1.create_bucket(s3, "fuag")
