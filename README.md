# Kiro Management API

Python module for programmatically creating Kiro subscription assignments using AWS SigV4 authentication.

## Prerequisites

1. **AWS Credentials** - Must be configured with appropriate credentials via:
   - `aws configure` command
   - IAM roles (for EC2 instances)
   - Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. **Python 3.6+**
3. **boto3** - Install with `pip install boto3`
4. **requests** - Install with `pip install requests`
5. **Permissions** - Your AWS credentials must have:
   - `q:CreateAssignment` permission

## Usage

### Creating Assignments

```python
from create_assignment import create_assignment

# Create a subscription assignment for a user or group
response = create_assignment(
    principal_id="12345678-1234-1234-1234-123456789abc",
    principal_type="USER",
    subscription_type="Q_DEVELOPER_STANDALONE_PRO"
)

print(response.status_code)
print(response.text)
```

### Listing User Subscriptions

```python
from list_user_subscriptions import list_user_subscriptions

# List user subscriptions for an instance
response = list_user_subscriptions(
    instance_arn="arn:aws:sso:::instance/ssoins-1234567890abcdef"
)

print(response.status_code)
print(response.text)
```

## Parameters

### create_assignment()

- `principal_id` (required): The ID of the user or group from IAM Identity Center
- `principal_type` (optional): Type of principal. Valid values:
  - `"USER"` (default)
  - `"GROUP"`
- `subscription_type` (optional): Type of subscription. Valid values:
  - `"Q_DEVELOPER_STANDALONE_PRO"` (default)
  - `"Q_DEVELOPER_STANDALONE_PRO_PLUS"`
  - `"Q_DEVELOPER_STANDALONE_POWER"`

### list_user_subscriptions()

- `instance_arn` (required): The ARN of the IAM Identity Center instance
- `max_results` (optional): Maximum number of results to return (default: 1000)
- `subscription_region` (optional): AWS region for subscriptions (default: "us-east-1")

## File Structure

- `create_assignment.py` - Module for creating Kiro subscription assignments
- `list_user_subscriptions.py` - Module for listing user subscriptions
