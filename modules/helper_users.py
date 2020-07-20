# A helper script to create a user with specified policy and return aws credentials.
# enumy / privy / persisty / exfily
import boto3
import json

# Use default session for now (maybe look to grab from environment variable for terraform runs.)
session = boto3.session.Session(profile_name='default')
iam = session.client('iam')


def usercheck(userid):
    if userid == 1:
        user = 'enuumy'
    if userid == 2:
        user = 'persisty'
    return user
    

def createuser(username):
    user = usercheck(username)
    if user:
        # Create user
        iam.create_user(UserName=user)
        with open('modules/policies/' + user +'.json') as json_file:
            policy_json = json.load(json_file)
        iam.put_user_policy(UserName=user, PolicyName=user, PolicyDocument=json.dumps(policy_json))

        # Generate new access key pair
        key_response = iam.create_access_key(UserName=user)
        return key_response

def destroyuser(username,accesskey):
    user = usercheck(username)
    if user:
        iam.delete_access_key(UserName=user, AccessKeyId=accesskey)
        iam.delete_user_policy(UserName=user, PolicyName=user)
        iam.delete_user(UserName=user)

# test block
#data = createuser(1)
#ak = data['AccessKey']['AccessKeyId']
#sk = data['AccessKey']['SecretAccessKey']

#destroyuser(1,ak)