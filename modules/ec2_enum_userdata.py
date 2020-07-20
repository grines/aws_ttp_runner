# AWS TTP Discovery / Enumerate EC2 UserData
# Hashicorp
import boto3
import base64
import time

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']

def listActions():
    print('DescribeInstances ✓')
    print('DescribeInstanceAttribute ✓')


def userdata(region,ak,sk):
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    ec2 = session.resource('ec2')
    for instance in ec2.instances.all():
        response = instance.describe_attribute(Attribute='userData')
        if 'UserData' in response and response['UserData']:
            base64.b64decode(response['UserData']['Value'])

def ec2_enum_userdata(ak,sk):
    print('\nExecuting EC2 UserData enumeration:')
    for region in regions:
        userdata(region,ak,sk)
    listActions()