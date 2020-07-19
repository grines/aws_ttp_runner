# AWS TTP Discovery / Alternatuve enumeration of users, roles, groups, and policies
# GetAuthorizationDetails
# Hashicorp Red
import boto3


# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')
client = session.client('iam')

print('---Users---')
print(client.get_account_authorization_details(Filter=['User']))
print('---End---\n')

print('---Groups---')
print(client.get_account_authorization_details(Filter=['Group']))
print('---End---\n')

print('---Roles---')
print(client.get_account_authorization_details(Filter=['Role']))
print('---End---\n')

print('---Local Managed Policies---')
print(client.get_account_authorization_details(Filter=['LocalManagedPolicy']))
print('---End---\n')

print('---AWS Managed Policies---')
print(client.get_account_authorization_details(Filter=['AWSManagedPolicy']))
print('---End---\n')