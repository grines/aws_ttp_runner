# AWS TTP Discovery / Network Enumeration
# DescribeAddresses DescribeCustomerGateways DescribeHosts DescribeInstances DescribeLaunchTemplates
# DescribeNatGateways DescribeNetworkAcls DescribeNetworkInterfaces
# DescribeRouteTabes DescribeSecurityGroups DescribeSubnets DescribeVpcEndpoints DescribeVpcs
# Hashicorp Red
import boto3
import time

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']

def listActions():
    print('DescribeAddresses ✓')
    print('DescribeCustomerGateways ✓')
    print('DescribeHosts ✓')
    print('DescribeInstances ✓')
    print('ListLaunchTemplates ✓')
    print('DescribeNatGateways ✓')
    print('DescribeNetworkAcls ✓')
    print('DescribeNetworkInterfaces ✓')
    print('DescribeRouteTables ✓')
    print('DescribeSecurityGroups ✓')
    print('DescribeSubnets ✓')
    print('DescribeVpcEndpoints ✓')
    print('DescribeVpcs ✓')


def network(region,ak,sk):
    session = boto3.session.Session(aws_access_key_id=ak, aws_secret_access_key=sk, region_name=region)
    ec2 = session.client('ec2')

    # Actions
    ec2.describe_addresses()
    ec2.describe_customer_gateways()
    ec2.describe_hosts()
    ec2.describe_instances()
    ec2.describe_launch_templates()
    ec2.describe_nat_gateways()
    ec2.describe_network_acls()
    ec2.describe_network_interfaces()
    ec2.describe_route_tables()
    ec2.describe_security_groups()
    ec2.describe_subnets()
    ec2.describe_vpc_endpoints()
    ec2.describe_vpcs()

def enum_network(ak,sk):
    print('\nExecuting EC2 Network enumeration:')
    for region in regions:
        network(region,ak,sk)
    listActions()