import json
import os
import ConfigParser

def load_config(profile_name):
    """Load API Keys from default locations"""
    home = os.path.expanduser('~')
    config_file = os.path.sep.join([home, '.tencentcloud', 'credentials'])
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    
    secret_id = config.get(profile_name, 'SecretId')
    secret_key = config.get(profile_name, 'SecretKey')
    app_id = config.get(profile_name, 'AppId')
    
    return [secret_id, secret_key, app_id]
