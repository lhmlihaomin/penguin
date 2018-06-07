import time
import random
import urllib
import requests
from collections import OrderedDict

from .common import load_config, public_params, raw_request


class Client(object):
    """
    API Client to operate TencentCloud load balancers.
    """
    def __init__(self, profile_name, region_name):
        self.method = 'GET'
        self.endpoint = 'lb.api.qcloud.com/v2/index.php'
        self.sign_method = 'HmacSHA256'

        self.profile_name = profile_name
        self.region_name = region_name

        secret_id, secret_key, app_id = load_config(profile_name)
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.app_id = app_id

    def describe_lb_health(self, load_balancer_id):
        params = public_params(self.region_name, self.secret_id)
        # get backend instance information (LAN IP & instance Id):
        params.update(
            {
                'Action': 'DescribeLoadBalancerBackends',
                'loadBalancerId': load_balancer_id,
            }
        )
        resp = raw_request(self.secret_key, self.method, self.endpoint, params)
        resp = resp['backendSet']
        instance_dict = {}
        for backend in resp:
            instance_dict.update({
                backend['lanIp']: backend['unInstanceId']
            })
        
        # get instance health status:
        params.update(
            {
                'Action': 'DescribeLBHealthStatus',
                'loadBalancerId': load_balancer_id,
            }
        )
        resp = raw_request(self.secret_key, self.method, self.endpoint, params)
        resp = resp['data']

        # reconstruct result in human readable way:
        result = {}
        for status in resp:
            if status['healthStatus'] == 1:
                health = True
            else:
                health = False
            result.update({
                instance_dict[status['ip']]: health
            })
        return result

    def register_instances_with_lb(self, load_balancer_name, instance_ids):
        pass

    def deregister_instances_from_lb(self, load_balancer_name, instance_ids):
        pass
