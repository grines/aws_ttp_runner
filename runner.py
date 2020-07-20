# Simple AWS TTP Runner
# Hashicorp Red
import boto3
import time
# Discovery modules
from modules.ec2_enum_userdata import ec2_enum_userdata
from modules.enum_network import enum_network
from modules.enum_secrets import enum_secrets
from modules.iam_enum import iam_enumv1
from modules.iam_enum2 import iam_enumv2
from modules.lambda_enum import lambda_enum
# Persistence modules
from modules.persist_AccessKey import iam_persist
# Helper modules
from modules.helper_users import createuser, destroyuser


### Enumeration/Discovery TTPs
# Create enumeration user
enuumy = createuser(1)
time.sleep(10) # wait for credentials to register
# TTPs
ec2_enum_userdata(enuumy['AccessKey']['AccessKeyId'],enuumy['AccessKey']['SecretAccessKey'])
enum_network(enuumy['AccessKey']['AccessKeyId'],enuumy['AccessKey']['SecretAccessKey'])
enum_secrets(enuumy['AccessKey']['AccessKeyId'],enuumy['AccessKey']['SecretAccessKey'])
iam_enumv1(enuumy['AccessKey']['AccessKeyId'],enuumy['AccessKey']['SecretAccessKey'])
iam_enumv2(enuumy['AccessKey']['AccessKeyId'],enuumy['AccessKey']['SecretAccessKey'])
lambda_enum(enuumy['AccessKey']['AccessKeyId'],enuumy['AccessKey']['SecretAccessKey'])

# Destroy enumeration user
destroyuser(1,enuumy['AccessKey']['AccessKeyId'])


### Persistence TTPs
# Create persistence user
persisty = createuser(2)
# TTPs
iam_persist(persisty['AccessKey']['AccessKeyId'],persisty['AccessKey']['SecretAccessKey'])
# Destroy persistence user
destroyuser(2,persisty['AccessKey']['AccessKeyId'])


### Privilege Escalation TTPs
# Create enuumy user
#privvy = createuser(3)
# TTPs

# Destroy privilege escalation user
#destroyuser(3,privvy['AccessKey']['AccessKeyId'])