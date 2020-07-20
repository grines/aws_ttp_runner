# AWS TTP Discovery / Enumerate secrets in secrets manager and parameters store
# DescribeParameters ListSecrets
# Hashicorp Red
import boto3
import time


def listActions():
    print('DescribeParameters ✓')
    print('ListSecrets ✓')

def enum_secrets(ak,sk):
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name='us-east-1')
    client_ssm = session.client('ssm')
    client_secrets = session.client('secretsmanager')
    print('\nExecuting Secrets Enumeration:')

    client_ssm.describe_parameters()
    client_secrets.list_secrets()
    listActions()

