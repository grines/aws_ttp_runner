# AWS TTP Discovery / Enumerate users, groups, roles, and policies
# ListGroups, ListRoles, ListPolicies, ListAttachedUserPolicies, ListGroupsForUser, ListMFADevices, ListUserPolicies, ListUsers
# Hashicorp Red
import boto3


# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')
client = session.client('iam')

def iam_enum():
    # Store users list
    users = client.list_users()
    user_list = []

    groups = client.list_groups()
    print('---Groups---')
    for g in groups['Groups']:
      print(g['GroupName'])
    print('---End Groups---\n')

    roles = client.list_roles()
    print('---Roles---')
    for r in roles['Roles']:    
        print(r['RoleName'])
    print('---End Roles---\n')

    policies = client.list_policies()
    print('---Policies---')
    for p in policies['Policies']:
        print(p['PolicyName'])
    print('---End Policies---\n')

    # loop through and enumerate users
    print('---User Details---')
    for key in users['Users']:
        result = {}
        Policies = []
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

    for key in user_list:
        print(key)
