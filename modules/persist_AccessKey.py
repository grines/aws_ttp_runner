# AWS TTP Discovery / Alternatuve enumeration of users, roles, groups, and policies
# GetAuthorizationDetails
# Hashicorp Red
import boto3
import time

def iam_persist(ak,sk):
    time.sleep(10)
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name='us-east-1')
    iam = session.client('iam')
    key_response = iam.create_access_key(UserName='persisty')
    time.sleep(10)
    iam.delete_access_key(UserName='persisty', AccessKeyId=key_response['AccessKey']['AccessKeyId'])
    return key_response


