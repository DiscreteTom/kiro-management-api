import boto3
import json
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
import requests


def create_assignment(principal_id, principal_type="USER", subscription_type="Q_DEVELOPER_STANDALONE_PRO"):
    """Create Q Developer subscription assignment"""
    
    session = boto3.Session()
    credentials = session.get_credentials()
    
    payload = {
        "principalId": principal_id,
        "principalType": principal_type,
        "subscriptionType": subscription_type
    }
    
    request = AWSRequest(
        method="POST",
        url="https://codewhisperer.us-east-1.amazonaws.com/",
        data=json.dumps(payload),
        headers={
            "Content-Type": "application/x-amz-json-1.0",
            "x-amz-target": "AmazonQDeveloperService.CreateAssignment",
        },
    )
    
    SigV4Auth(credentials, "q", "us-east-1").add_auth(request)
    
    response = requests.post(request.url, headers=dict(request.headers), data=request.body)
    
    return response
