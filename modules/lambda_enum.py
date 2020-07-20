# AWS TTP Discovery / Enumerate Lambda functions
# Hashicorp
import boto3
import time

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']

def listActions():
    print('ListFunctions ✓')

def lambdas(region,ak,sk):
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    lam = session.client('lambda')
    lam.list_functions()

def lambda_enum(ak,sk):
    print('\nExecuting lambda enumeration:')
    for region in regions:
        lambdas(region,ak,sk)
    listActions()