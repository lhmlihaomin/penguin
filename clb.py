import time
import random
import urllib
import requests
import hashlib
import base64
import hmac
from collections import OrderedDict

#from tencentcloud.common.sign import Sign
from tencent.common import sign_query

now = int(time.time())
nonce = random.randint(1, 10000)

method = 'GET'
endpoint = 'lb.api.qcloud.com/v2/index.php'
sign_method = 'HmacSHA256'
secret_id = ""
secret_key = ""

params = {
    'Action': 'DescribeLBHealthStatus',
    'loadBalancerId': 'lb-lu1p3giv',
    'Region': 'ap-shanghai',
    'Timestamp': now,
    'Nonce': nonce,
    'SecretId': secret_id,
    "SignatureMethod" : "HmacSHA256",
}

"""
od = OrderedDict(sorted(params.items(), key=lambda x: x[0]))
query = urllib.urlencode(od)
message = method+endpoint+'?'+query
#sig = Sign.sign(secret_key, message, sign_method)
sig = base64.encodestring(
    hmac.new(secret_key, message, hashlib.sha256).digest()
)[:-1]
sig = urllib.quote(sig)
sig = sig.replace('/', '%2F')
print sig"""

query = sign_query(secret_key, method, endpoint, params)

url = "https://" + endpoint + "?" + query
print url
