# AWS TTP Discovery / Network Enumeration
# DescribeAddresses DescribeCustomerGateways DescribeHosts DescribeInstances DescribeLaunchTemplates
# DescribeNatGateways DescribeNetworkAcls DescribeNetworkInterfaces
# DescribeRouteTabes DescribeSecurityGroups DescribeSubnets DescribeVpcEndpoints DescribeVpcs
# Hashicorp Red
import boto3

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')

def network(region):
    client = boto3.client('ec2', region_name=region)
    print('---Region ' + region + '---\n\n')

    print('---List Addresses---')
    print(client.describe_addresses())
    print('---End---\n')
    
    print('---List Customer Gateways---')
    print(client.describe_customer_gateways())
    print('---End---\n')

    print('---List Hosts---')
    print(client.describe_hosts())
    print('---End---\n')

    print('---List Instances---')
    print(client.describe_instances())
    print('---End---\n')

    print('---List Launch Templates---')
    print(client.describe_launch_templates())
    print('---End---\n')

    print('---List Nat Gateways---')
    print(client.describe_nat_gateways())
    print('---End---\n')

    print('---List Network ACLs---')
    print(client.describe_network_acls())
    print('---End---\n')

    print('---List Network Interfaces---')
    print(client.describe_network_interfaces())
    print('---End---\n')

    print('---List Network Interfaces---')
    print(client.describe_route_tables())
    print('---End---\n')

    print('---List Network Interfaces---')
    print(client.describe_security_groups())
    print('---End---\n')

    print('---List Network Interfaces---')
    print(client.describe_subnets())
    print('---End---\n')

    print('---List Network Interfaces---')
    print(client.describe_vpc_endpoints())
    print('---End---\n')

    print('---List Network Interfaces---')
    print(client.describe_vpcs())
    print('---End---\n')

for region in regions:
    enum = network(region)