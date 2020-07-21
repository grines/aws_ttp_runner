# A helper script to create a user with specified policy and return aws credentials.
# enumy / privy / persisty / exfily
import boto3
import json
import time

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')

users = ['persisty','enuumy','privvy','dummmy']
roles = ['OrganizationalAdminRole','SSM_EC2_Role']
policies =[]

def cleanup_users(user):
    iam = session.client('iam')

    keys = iam.list_access_keys(UserName=user,MaxItems=2)
    print(keys)
    for key in keys['AccessKeyMetadata']:
        iam.delete_access_key(UserName=user, AccessKeyId=key['AccessKeyId'])
    iam.delete_user_policy(UserName=user, PolicyName=user)
    iam.delete_user(UserName=user)

def cleanup_roles(RoleName):
    resource = session.resource('iam')
    role = resource.Role(name=RoleName)

    # Get all Managed Policies and detatch them
    for policy in role.attached_policies.all():
        print(f"Removing Managed Policy from {role.name}")
        role.detach_policy(PolicyArn=policy.arn)

     # Get all Instance Profiles and detatch them
    for profile in role.instance_profiles.all():
        print(f"Removing role from InstanceProfile {profile.name}")
        profile.remove_role(RoleName=role.name)

    # Get all Inline Policies and delete them
    for role_policy in role.policies.all():
        print(f"Deleting Policy {role_policy.name}")
        role_policy.delete()

    role.delete()
    print(f"{role.name} deleted\n")

def cleanup_policies():
    iam = session.client('iam')
    response = iam.delete_instance_profile(InstanceProfileName='SSM_EC2_Role')
    response = iam.delete_policy(PolicyArn='arn:aws:iam::240213749104:policy/SSM_EC2')
    print(response)

def cleanup_e2s():
    print('Clean EC2s by tag')

def cleanup_lambdas():
    print('Clean Lambdas by tag')

def clean():
    for role in roles:
        try:
            cleanup_roles(role)
        except:
            pass

    for user in users:
        try:
            cleanup_users(user)
        except:
            pass
    try:
        cleanup_policies()
    except:
        pass

clean()