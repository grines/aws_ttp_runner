# AWS TTP Discovery / Alternatuve enumeration of users, roles, groups, and policies
# GetAuthorizationDetails
# Hashicorp Red
import boto3
import time

def listActions():
    print('GetAccountAuthorizationDetails -User ✓')
    print('GetAccountAuthorizationDetails -Group ✓')
    print('GetAccountAuthorizationDetails -Role ✓')
    print('GetAccountAuthorizationDetails -LocalManagedPolicy ✓')
    print('GetAccountAuthorizationDetails -AWSManagedPolicy ✓')


def iam_enumv2(ak,sk):
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name='us-east-1')
    client = session.client('iam')
    print('\nExecuting IAM Enumeration v2:')

    client.get_account_authorization_details(Filter=['User'])
    client.get_account_authorization_details(Filter=['Group'])
    client.get_account_authorization_details(Filter=['Role'])
    client.get_account_authorization_details(Filter=['LocalManagedPolicy'])
    client.get_account_authorization_details(Filter=['AWSManagedPolicy'])
    listActions()
