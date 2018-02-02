import sys
from client import QcloudClient

instance_ids = sys.argv[1:]

client = QcloudClient()
#result = client.describe_instances()
#result = client.stop_instances(instance_ids)
result = client.start_instances(instance_ids)
print result

