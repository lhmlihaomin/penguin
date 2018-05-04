import sys
from client import QcloudClient

instance_ids = sys.argv[1:]

client = QcloudClient()
#result = client.describe_instances()
#result = client.stop_instances(instance_ids)
#result = client.start_instances(instance_ids)
"""
params = {
    'Zone': 'ap-shanghai-1',
    'InstanceType': 'S1.SMALL1',
    'ImageId': 'img-pyqx34y1',
    'VpcId': 'vpc-b5ifw0o0',
    'SubnetId': 'subnet-atxqe1nh',
    'InstanceCount': 2,
    'KeyId': 'skey-54zgrhjn',
    'SecurityGroupId': 'sg-g1bkvohw',
}
result = client.run_instances(params)
"""

#params = {
#    'InstanceIds': ['ins-kub5cfu5', 'ins-3uf795ut'],
#    'InstanceName': 'prd-apitest-1.0.0-sh1-000'
#}
#result = client.modify_instances_attribute(params)

result = client.terminate_instances(instance_ids)

print result

