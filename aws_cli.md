# AWS CLI Cheatsheet

## Configuration & Authentication
```bash
# Configure AWS CLI
aws configure

# List configured profiles
aws configure list-profiles

# Use specific profile
aws --profile [profile-name] [command]
```

## S3 Operations
```bash
# List buckets
aws s3 ls

# List contents of bucket
aws s3 ls s3://bucket-name

# Copy local file to S3
aws s3 cp file.txt s3://bucket-name/

# Copy S3 file to local
aws s3 cp s3://bucket-name/file.txt ./

# Sync directory to S3
aws s3 sync . s3://bucket-name/

# Delete file from S3
aws s3 rm s3://bucket-name/file.txt

# Delete bucket
aws s3 rb s3://bucket-name --force
```

## EC2 Operations
```bash
# List instances
aws ec2 describe-instances

# Start instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Stop instance
aws ec2 stop-instances --instance-ids i-1234567890abcdef0

# Create instance
aws ec2 run-instances --image-id ami-12345678 --instance-type t2.micro --key-name MyKeyPair

# Terminate instance
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

## Security Groups
```bash
# List security groups
aws ec2 describe-security-groups

# Create security group
aws ec2 create-security-group --group-name my-sg --description "My security group"

# Add inbound rule
aws ec2 authorize-security-group-ingress --group-id sg-123456 --protocol tcp --port 22 --cidr 0.0.0.0/0
```

## IAM Operations
```bash
# List users
aws iam list-users

# Create user
aws iam create-user --user-name username

# Add user to group
aws iam add-user-to-group --user-name username --group-name groupname

# Create access key
aws iam create-access-key --user-name username
```

## Lambda Operations
```bash
# List functions
aws lambda list-functions

# Invoke function
aws lambda invoke --function-name my-function output.txt

# Update function code
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
```

## RDS Operations
```bash
# List DB instances
aws rds describe-db-instances

# Create DB snapshot
aws rds create-db-snapshot --db-instance-identifier mydb --db-snapshot-identifier mydb-snapshot

# Delete DB instance
aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot
```

## CloudWatch Operations
```bash
# Get metrics
aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization

# Put metric data
aws cloudwatch put-metric-data --namespace MyNamespace --metric-name MyMetric --value 100

# Describe alarms
aws cloudwatch describe-alarms
```

## Common Options
```bash
--region [region-name]    # Specify AWS region
--output [json|text|table]    # Output format
--profile [profile-name]    # Use specific profile
--debug    # Get debug output
--version    # Display AWS CLI version
```

Would you like me to add any specific AWS service commands or explain any of these commands in more detail?
