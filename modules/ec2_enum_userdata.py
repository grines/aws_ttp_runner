# AWS TTP Discovery / Enumerate EC2 UserData
# Hashicorp
import boto3
import base64

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')

def userdata(region):
    ec2 = session.resource('ec2', region_name=region)
    for instance in ec2.instances.all():
        response = instance.describe_attribute(Attribute='userData')
        if 'UserData' in response and response['UserData']:
            raw_userdata = base64.b64decode(response['UserData']['Value'])
            print('---User Data---')
            print(raw_userdata)
            print('---User Data End---\n')

def ec2_enum_userdata():
    for region in regions:
        userdata(region)