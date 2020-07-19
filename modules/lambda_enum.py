# AWS TTP Discovery / Enumerate Lambda functions
# Hashicorp
import boto3

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')

def lambdas(region):
    lam = session.client('lambda', region_name=region)
    response = lam.list_functions()
    for r in response['Functions']:
        print('---Lambda Functions---')
        print(r)
        print('---Lambda Functions End---\n')

for region in regions:
    secrets = lambdas(region)