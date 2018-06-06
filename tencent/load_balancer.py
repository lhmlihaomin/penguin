import time
import random
import urllib
import requests
from collections import OrderedDict

from .common import public_params

method = 'GET'
endpoint = 'lb.api.qcloud.com/v2/index.php'
sign_method = 'HmacSHA256'


class Clinet(object):
    """
    API Client to operate TencentCloud load balancers.
    """
    def __init__(self, profile_name, region_name):
        self.profile_name = profile_name
        self.region_name = region_name

        secret_id, secret_key, app_id = load_config(profile_name)
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.app_id = app_id

    def describe_lb_health(self, load_balancer_name):
        params = public_params(self.region_name, self.secret_id)
        params.update(
            {
                'Action': 'DescribeLBHealthStatus',
                'loadBalancerId': ''
            }
        )
        pass

    def register_instances_with_lb(self, load_balancer_name, instance_ids):
        pass

    def deregister_instances_from_lb(self, load_balancer_name, instance_ids):
        pass
