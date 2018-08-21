import os
import hashlib

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

from .common import load_config

class Client(object):
    """
    API Client to operate TencentCloud COS objects.
    """
    def __init__(self, profile_name, region_name):
        secret_id, secret_key, app_id = load_config(profile_name)
        self.app_id = app_id
        self.config = CosConfig(
            Secret_id=secret_id,
            Secret_key=secret_key,
            Region=region_name
            )
        self.client = CosS3Client(self.config)

    def file_md5(self, local_path):
        #file_size = os.path.getsize(local_path)        
        with open(local_path, 'rb') as fp:
            file_hash = hashlib.md5(fp.read())
        return file_hash.hexdigest()
            

    def download_file(self, bucket, key, local_path):
        bucket = '-'.join([bucket, self.app_id])
        resp = self.client.get_object(bucket, key)
        resp['Body'].get_stream_to_file(local_path)

    def upload_file(self, bucket, key, local_path):
        bucket = '-'.join([bucket, self.app_id])
        file_md5 = self.file_md5(local_path)
        print "file md5:   "+file_md5
        with open(local_path, 'r') as fp:
            response = self.client.put_object(bucket, fp, key)
            print "upload md5: "+response['Etag']
        return file_md5 == response['Etag'][1:-1]

    def upload_file_ex(self, bucket, key, local_path):
        bucket = '-'.join([bucket, self.app_id])
        file_md5 = self.file_md5(local_path)
        print "file md5:   "+file_md5
        response = self.client.upload_file(
            Bucket=bucket,
            Key=key,
            LocalFilePath=local_path   
        )
        print "upload md5: "+response['Etag']

        # API doesn't return anything when using multipart upload,
        # so just return True.
        return True
        #return file_md5 == response['Etag'][1:-1]
