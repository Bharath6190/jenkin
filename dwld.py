##
## Author : Bhaskar Varadaraju
## A Python3 program to Download an existing file from AWS S3
##       
## ******  IMPORTANT : Set below before executing ******
##  export AWS_ACCESS_KEY_ID=AKIASICPKLFQGZY23CCM
##  export AWS_SECRET_ACCESS_KEY=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
##
import boto3
import os

""" Input:
export S3_DOWNLOAD_FILENAME='03_s3_bucket_download_file.py'
export S3_DOWNLOAD_LOCALNAME='/home/ubuntu/Downloads'
export S3_BUCKET_NAME='git619'
"""

def download_from_aws_s3(bucket, remote_file, local_file):
    print("Downloading file : ", remote_file)
    s3_client = boto3.client('s3',
        region_name='ap-south-1',
    )
    s3_client.download_file(bucket, remote_file, local_file)

s3_file_name      = os.environ.get('03_s3_bucket_download_file.py')
s3_local_filepath = os.environ.get('/home/ubuntu/Downloads')
s3_bucket_name    = os.environ.get('git619')

download_from_aws_s3( git619, 03_s3_bucket_download_file.py,home/ubuntu/Downloads )

