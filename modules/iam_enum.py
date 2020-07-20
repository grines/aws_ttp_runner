# AWS TTP Discovery / Enumerate users, groups, roles, and policies
# ListGroups, ListRoles, ListPolicies, ListAttachedUserPolicies, ListGroupsForUser, ListMFADevices, ListUserPolicies, ListUsers
# Hashicorp Red
import boto3
import time

def listActions():
    print('ListUsers ✓')
    print('ListGroups ✓')
    print('ListRoles ✓')
    print('ListPolicies ✓')
    print('ListUserPolicies ✓')
    print('ListAttachedUserPolicies ✓')
    print('ListGroupsForUser ✓')
    print('ListMFADevices ✓')

def iam_enumv1(ak,sk):
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name='us-east-1')
    client = session.client('iam')
    print('\nExecuting IAM Enumeration v1:')

    # Store users list
    users = client.list_users()
    user_list = []

    client.list_groups()
    client.list_roles()
    client.list_policies()

    # loop through and enumerate users
    for key in users['Users']:
        result = {}
        Groups=[]
        Managed_Policies=[]

        result['userName']=key['UserName']

        # Grab user policies
        List_of_Policies =  client.list_user_policies(UserName=key['UserName'])
        result['Policies'] = List_of_Policies['PolicyNames']

        # Grab managed policies
        managed_user_policies = client.list_attached_user_policies(UserName=key['UserName'])
        for Policy in managed_user_policies['AttachedPolicies']:
          Managed_Policies.append(Policy['PolicyName'])
        result['Managed_Policies'] = Managed_Policies

        # Grab Groups for user
        List_of_Groups =  client.list_groups_for_user(UserName=key['UserName'])
        for Group in List_of_Groups['Groups']:
            Groups.append(Group['GroupName'])
        result['Groups'] = Groups

        # Check for MFA
        List_of_MFA_Devices = client.list_mfa_devices(UserName=key['UserName'])
        if not len(List_of_MFA_Devices['MFADevices']):
            result['isMFADeviceConfigured']=False   
        else:
            result['isMFADeviceConfigured']=True    
        user_list.append(result)
    listActions()