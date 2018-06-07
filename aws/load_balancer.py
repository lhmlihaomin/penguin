import boto3

class Client(object):
    """
    AWS ELB related operations.
    """
    def __init__(self, profile_name, region_name):
        self.profile_name = profile_name
        self.region_name = region_name

        self.elb = boto3.Session(
            profile_name=self.profile_name,
            region_name=self.region_name
        ).client('elb')

    def describe_lb_health(self, load_balancer_name):
        response = self.elb.describe_instance_health(
            LoadBalancerName=load_balancer_name
        )
        response = response['InstanceStates']
        result = {}
        for state in response:
            result.update({
                state['InstanceId']: state['State'] == 'InService'
            })
        return result
        