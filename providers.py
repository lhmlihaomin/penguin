import importlib


class Provider(object):

    services = {
        'aws': [
            'ec2',
            'object_store',
        ],
        'tencent': [
            'cos'
        ]
    }

    def __init__(self, name, profile_name, region_name):
        self.name = name
        self.profile_name = profile_name
        self.region_name = region_name

    def client(self, service_name):
        if self.services.has_key(self.name):
            if service_name in self.services[self.name]:
                module_name = ".".join([self.name, service_name])
                module = importlib.import_module(module_name, package='.')
                client = module.Client(self.profile_name, self.region_name)
                return client
        raise Exception("Not supported.")
