# AWS TTP Discovery / Enumerate secrets in secrets manager and parameters store
# DescribeParameters ListSecrets
# Hashicorp Red
import boto3


# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')
client = session.client('ssm')
client2 = session.client('secretsmanager')

def enum_secrets():
    print('---List secrets in SSM---')
    print(client.describe_parameters())
    print('---End---\n')

    print('---List secrets in Secrets Manager---')
    print(client2.list_secrets())
    print('---End---\n')

