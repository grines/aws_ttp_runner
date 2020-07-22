# A helper script to create a user with specified policy and return aws credentials.
# enumy / privy / persisty / exfily
import boto3
import json
import time
from botocore.exceptions import ClientError

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')

users = ['persisty','enuumy','privvy','dummmy']
roles = ['OrganizationalAdminRole','SSM_EC2_Role']
policies =[]

def cleanup_users(user):
    iam = session.client('iam')
    try:
        iam.get_user(UserName=user)
    except ClientError as e:
        print(e)
        return True
    keys = iam.list_access_keys(UserName=user,MaxItems=2)
    for key in keys['AccessKeyMetadata']:
        iam.delete_access_key(UserName=user, AccessKeyId=key['AccessKeyId'])
        iam.delete_user_policy(UserName=user, PolicyName=user)
        iam.delete_user(UserName=user)
    return True

def cleanup_roles(RoleName):
    resource = session.resource('iam')
    role = resource.Role(name=RoleName)

    # Get all Managed Policies and detatch them
    try:
        for policy in role.attached_policies.all():
            role.detach_policy(PolicyArn=policy.arn)
    except ClientError as e:
        print(e)
        return True

     # Get all Instance Profiles and detatch them
    for profile in role.instance_profiles.all():
        #print(f"Removing role from InstanceProfile {profile.name}")
        profile.remove_role(RoleName=role.name)

    # Get all Inline Policies and delete them
    for role_policy in role.policies.all():
        #print(f"Deleting Policy {role_policy.name}")
        role_policy.delete()

    role.delete()
    return True

def cleanup_policies():
    iam = session.client('iam')
    try:
        iam.delete_instance_profile(InstanceProfileName='SSM_EC2_Role')
    except ClientError as e:
        print(e)
        pass
    try:
        iam.delete_instance_profile(InstanceProfileName='OrganizationalAdminRole')
    except ClientError as e:
        print(e)
        pass
    try:
        iam.delete_policy(PolicyArn='arn:aws:iam::240213749104:policy/SSM_EC2')
    except ClientError as e:
        print(e)
        pass
    return True

def cleanup_ec2s():
    client = session.client('ec2')
    #print('Terminate EC2s by Runner tag')
    custom_filter = [{
    'Name':'tag:Runner', 
    'Values': ['1']}]
    instances = client.describe_instances(Filters=custom_filter)
    for instance in instances['Reservations']:
        for i in instance['Instances']:
            #print(i['InstanceId'])
            client.terminate_instances(InstanceIds=[i['InstanceId']])
    return True

def cleanup_lambdas():
    client = session.client('lambda')
    try:
        client.delete_function(FunctionName='OrgUpdate')
    except ClientError as e:
        print(e)
        pass
    return True

def clean():
    print('-----\n\nRunning Account Cleaning:')
    for role in roles:
        cleanup_roles(role)

    for user in users:
        cleanup_users(user)
        
    cleanup_policies()
    cleanup_lambdas()
    cleanup_ec2s()

#clean()