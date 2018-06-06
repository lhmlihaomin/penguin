import json
import os
import ConfigParser
import urllib
import hashlib
import base64
import hmac
import requests
import time
import random
from collections import OrderedDict

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


def sort_params(params):
    """Use OrderedDict and sort params alphabetically by key"""
    od = OrderedDict(sorted(params.items(), key=lambda x: x[0]))
    return od


def sign_query(secret_key, method, endpoint, params):
    """Sign the request message"""
    if params.has_key('SignatureMethod'):
        if params['SignatureMethod'] == 'HmacSHA1':
            sig_method = hashlib.sha1
        elif params['SignatureMethod'] == 'HmacSHA256':
            sig_method = hashlib.sha256
    else:
        params.update({'SignatureMethod': 'HmacSHA256'})
        sig_method = hashlib.sha256
    sorted_params = sort_params(params)
    query = urllib.urlencode(sorted_params)
    message = method.upper()+endpoint+'?'+query
    print message
    sig = base64.encodestring(
        hmac.new(secret_key, message, sig_method).digest()
    )[:-1]
    print sig
    sig = urllib.quote(sig)
    sig = sig.replace('/', '%2F')
    print sig

    signed_query = query + '&Signature=' + sig
    return signed_query


def public_params(region, secret_id):
    """Build public params dict"""
    params = {
        'Region': region,
        'Timestamp': int(time.time()),
        'Nonce': random(1,10000),
        'SecretId': secret_id,
        "SignatureMethod" : "HmacSHA256",
    }


def raw_request(method, url, data):
    """Manually make request to endpoint with `requests` lib."""
    if method.upper() == 'GET':
        response = requests.get(url)
    elif method.upper() == 'POST':
        response = requests.post(url, data)
    return response.json()
