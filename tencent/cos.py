from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

from .common import load_config

class Client(object):
    """
    API Client to operate TencentCloud COS objects.
    """
    def __init__(self, profile_name, region_name):
        secret_id, secret_key = load_config(profile_name)
        self.config = CosConfig(
            Secret_id=secret_id,
            Secret_key=secret_key,
            Region=region_name
            )
        self.client = CosS3Client(self.config)

    def download_file(self, bucket, key, local_path):
        resp = self.client.get_object(bucket, key)
        resp['Body'].get_stream_to_file(local_path)

    def upload_file(self, bucket, key, local_path):
        pass
