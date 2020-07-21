# A helper script to create a user with specified policy and return aws credentials.
# enumy / privy / persisty / exfily
import boto3
import json
import time

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')
iam = session.client('iam')


def usercheck(userid):
    if userid == 1:
        user = 'enuumy'
    if userid == 2:
        user = 'persisty'
    if userid == 3:
        user = 'privvy'
    return user
    

def createuser(username):
    user = usercheck(username)
    if user:
        # Create user
        print('\n-----\n-Building ' + user + ' user-')
        iam.create_user(UserName=user)
        with open('modules/policies/' + user +'.json') as json_file:
            policy_json = json.load(json_file)
        iam.put_user_policy(UserName=user, PolicyName=user, PolicyDocument=json.dumps(policy_json))

        # Generate new access key pair
        key_response = iam.create_access_key(UserName=user)
        time.sleep(15) # wait for credentials to register
        return key_response

def destroyuser(username,accesskey):
    user = usercheck(username)
    if user:
        print('\n-Destroying ' + user + ' user-\n-----\n')
        iam.delete_access_key(UserName=user, AccessKeyId=accesskey)
        iam.delete_user_policy(UserName=user, PolicyName=user)
        iam.delete_user(UserName=user)
