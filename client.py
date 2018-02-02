import os, json
import ConfigParser

from QcloudApi.qcloudapi import QcloudApi

API_VERSION = '2017-03-12'

class QcloudClient(object):
    """Qcloud Client with handy features."""
    def __init__(self, profile_name='default'):
        self.profile_name = profile_name
        self.parse_config()
        self.parse_credentials()
        
    ##### Configuration methods #####
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

    ##### Result parsing #####
    def parse_result(self, action, result):
        result_keys = {
            'DescribeInstances': 'InstanceSet'
        }
        result = json.loads(result)
        result = result['Response']
        if result.has_key('Error'):
            return (False, result)
        if result_keys.has_key(action):
            return (True, result[result_keys[action]])
        else:
            return (True, result)

    ##### Service methods #####
    def set_service(self, module):
        """Set service object with module"""
        config = {
            'Region': self.region,
            'secretId': self.secret_id,
            'secretKey': self.secret_key,
            'method': 'post'
        }
        self.service = QcloudApi(module, config)

    def describe_instances(self):
        """List CVM instance information"""
        self.set_service('cvm')
        action = 'DescribeInstances'
        params = {'Version': '2017-03-12'}
        result = self.service.call(action, params)
        result = self.parse_result(action, result)
        return result

    def run_instances(self):
        pass

    def start_instances(self, instance_ids):
        """Start (boot) CVM instances"""
        self.set_service('cvm')
        action = 'StartInstances'
        params = {
            'Version': API_VERSION,
            'InstanceIds': instance_ids,
        }
        result = self.service.call(action, params)
        result = self.parse_result(action, result)
        return result

    def stop_instances(self, instance_ids):
        """Stop (shutdown) CVM instances"""
        self.set_service('cvm')
        action = 'StopInstances'
        params = {
            'Version': API_VERSION,
            'InstanceIds': instance_ids,
        }
        result = self.service.call(action, params)
        result = self.parse_result(action, result)
        return result

    def modify_instance_security_group(self):
        pass

    def modify_instance_tags(self):
        pass

    def modify_volume_tags(self):
        pass

