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

## Parameters

- `principal_id` (required): The ID of the user or group from IAM Identity Center
- `principal_type` (optional): Type of principal. Valid values:
  - `"USER"` (default)
  - `"GROUP"`
- `subscription_type` (optional): Type of subscription. Valid values:
  - `"Q_DEVELOPER_STANDALONE_PRO"` (default)
  - `"Q_DEVELOPER_STANDALONE_PRO_PLUS"`
  - `"Q_DEVELOPER_STANDALONE_POWER"`

## File Structure

- `create_assignment.py` - Module for creating Kiro subscription assignments
