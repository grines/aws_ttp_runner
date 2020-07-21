# AWS TTP Persistence / persistence create user
# CreateUser DeleteUser CreateAccessKey DeleteAccessKey
# Hashicorp Red
import boto3
import time

def listActions():
    print('CreateUser ✓')
    print('DeleteUser ✓')
    print('CreateAccessKey ✓')
    print('DeleteAccessKey ✓')

def createuser_persist(ak,sk):
    print('\nExecuting IAM CreateUser Peristence:')
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name='us-east-1')
    iam = session.client('iam')
    response = iam.create_user(UserName='dummmy')
    key_response = iam.create_access_key(UserName='dummmy')
    iam.delete_access_key(UserName='dummmy', AccessKeyId=key_response['AccessKey']['AccessKeyId'])
    iam.delete_user(UserName='dummmy')
    listActions()
    return response

