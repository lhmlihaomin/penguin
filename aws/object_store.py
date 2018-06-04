import os
import boto3

class Client(object):
    """Pseudo client for AWS S3 service"""
    def __init__(self, profile_name, region_name):
        self.profile_name = profile_name
        self.region_name = region_name

        self.s3 = boto3.Session(
            profile_name=self.profile_name,
            region_name=self.region_name
            ).resource('s3')

    def download_file(self, bucket, key, local_path):
        if key.startswith('/'):
            key = key[1:]
        bucket = self.s3.Bucket(bucket)
        bucket.download_file(key, local_path)
        

    def upload_file(self, bucket, key, local_path):
        if key.startswith('/'):
            key = key[1:]
        bucket = self.s3.Bucket(bucket)
        bucket.upload_file(local_path, key)
