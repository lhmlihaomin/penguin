#!/usr/bin/python
# Concept of the finished SDK.


# import package:
import penguin

# initialize cloud resource provider:
provider = penguin.Provider(
    provider_name="tencent",
    profile_name="cn-prd",
    region_name="ap-shanghai"
)

# initialize service:
service = provider.Service('cloud_server')

# calling API:
service.describe_instances(
    instance_ids=['i-12345678', 'i-xxxxxxxx'],
    filters={
        'state': 'running',
        'name': 'prd-connector-*'
    }
)

# calling another API:
service.create_instances(
    subnet_id='subnet-123',
    count=2,
    image_id='ami-12345678',
    security_group_ids=['sg-abcdef', ],
    key_name='prd-cnn1-cloud',
    instance_type='S3.SMALL1',
)

# initialize another service:
service = provider.Service('object_storage')

# calling API:
service.upload_file(
    bucket_name="personal",
    path="lihaomin/test.txt",
    local="/home/ubuntu/test.txt"
)
