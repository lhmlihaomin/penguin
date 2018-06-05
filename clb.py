import time
import random
import urllib
import requests
from collections import OrderedDict

from tencentcloud.common.sign import Sign

now = int(time.time())
nonce = random.randint(1, 10000)

method = 'GET'
endpoint = 'lb.api.qcloud.com/v2/index.php'
sign_method = 'HmacSHA256'
secret_id = "my_id"
secret_key = "my_key"

params = {
    'Action': 'DescribeLoadBalancerBackends',
    'loadBalancerId': 'lb_id',
    'Region': 'ap-shanghai',
    'Timestamp': now,
    'Nonce': nonce,
    'SecretId': secret_id,
    "SignatureMethod" : "HmacSHA256",
}

od = OrderedDict(sorted(params.items(), key=lambda x: x[0]))
query = urllib.urlencode(od)
message = method+endpoint+'?'+query
sig = Sign.sign(secret_key, message, sign_method)
sig = urllib.quote(sig)
sig = sig.replace('/', '%2F')
query = query + '&Signature=' + sig

url = "https://" + endpoint + "?" + query
print url
