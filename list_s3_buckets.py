from dotenv import load_dotenv
load_dotenv()

import os
import boto3

#s3 = boto3.resource('s3')
s3 = boto3.resource('s3', aws_access_key_id=os.environ.get("AWS_KEY_ID"),
                      aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"))

for bucket in s3.buckets.all():
    print(bucket.name)
