import os
import ConfigParser

from QcloudApi.qcloudapi import QcloudApi

class QcloudClient(object):
    """Qcloud Client with handy features."""
    @property
    def default_config_file(self):
        return os.path.sep.join([
            os.path.expanduser('~'),
            '.qcloud',
            'config'
        ])

    @property
    def default_credentials_file(self):
        return os.path.sep.join([
            os.path.expanduser('~'),
            '.qcloud',
            'credentials'
        ])

    def parse_config(self):
        """Configure with default config file"""
        parser = ConfigParser.ConfigParser()
        try:
            fp = open(self.default_config_file, 'r')
            parser.readfp(fp)
            fp.close()
            self.region = parser.get(self.profile_name, 'region')
        except:
            self.region = ''


    def parse_credentials(self):
        """Configure with default credentials file"""
        parser = ConfigParser.ConfigParser()
        try:
            fp = open(self.default_credentials_file, 'r')
            parser.readfp(fp)
            fp.close()
            self.secret_id = parser.get(self.profile_name, 'secret_id')
            self.secret_key = parser.get(self.profile_name, 'secret_key')
        except:
            self.secret_id = ''
            self.secret_key = ''

    def configure(self, region_name, secret_id, secret_key):
        """Manually configure"""
        self.region = region_name
        self.secret_id = secret_id
        self.secret_key = secret_key

    def __init__(self, profile_name='default'):
        self.profile_name = profile_name
        self.parse_config()
        self.parse_credentials()
        
    def service(module):
        config = {
            'Region': self.region,
            'secretId': self.secret_id,
            'secretKey': self.secret_key,
            'method': 'post'
        }
        QcloudApi(module, config)
