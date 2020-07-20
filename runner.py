# Simple AWS TTP Runner
# Hashicorp Red
from modules.ec2_enum_userdata import ec2_enum_userdata
from modules.enum_network import enum_network
from modules.enum_secrets import enum_secrets
from modules.iam_enum import iam_enum
from modules.iam_enum2 import iam_enum2
from modules.lambda_enum import lambda_enum


# Enumeration/Discovery TTPs
ec2_enum_userdata()
enum_network()
enum_secrets()
iam_enum()
iam_enum2()
lambda_enum()