import boto3
import json
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
import requests


def list_user_subscriptions(instance_arn, max_results=1000, subscription_region="us-east-1"):
    """List user subscriptions from AWS User Subscriptions service"""
    
    session = boto3.Session()
    credentials = session.get_credentials()
    
    payload = {
        "instanceArn": instance_arn,
        "maxResults": max_results,
        "subscriptionRegion": subscription_region
    }
    
    request = AWSRequest(
        method="POST",
        url="https://service.user-subscriptions.us-east-1.amazonaws.com/",
        data=json.dumps(payload),
        headers={
            "Content-Type": "application/x-amz-json-1.0",
            "x-amz-target": "AWSZornControlPlaneService.ListUserSubscriptions",
        },
    )
    
    SigV4Auth(credentials, "user-subscriptions", "us-east-1").add_auth(request)
    
    response = requests.post(request.url, headers=dict(request.headers), data=request.body)
    
    return response
