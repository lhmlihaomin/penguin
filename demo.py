#coding: utf8
#!/usr/bin/python
# Concept of the finished SDK.


# import package:
from providers import Provider

provider = Provider('tencent', 'default', 'ap-shanghai')
client = provider.client('cos')

client.download_file(
    bucket='test', 
    key='/download.txt',
    local_path=u'./local.txt'
)

result = client.upload_file(
	bucket='test',
	key='/upload.txt',
	local_path='./upload.txt'
)

print result
