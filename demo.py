#coding: utf8
#!/usr/bin/python
# Concept of the finished SDK.


# import package:
from providers import Provider

provider = Provider('aws', 'cn-alpha', 'cn-north-1')
client = provider.client('load_balancer')
#result = client.register_instances_with_lb(
#    'dev-elb-devConnectortest-cnn1-0',
#    ['i-0faa8346b5a4fdba8','i-056b4eb5634740edc']
#)

result = client.deregister_instances_from_lb(
    'dev-elb-devConnectortest-cnn1-0',
    ['i-056b4eb5634740edc']
)
