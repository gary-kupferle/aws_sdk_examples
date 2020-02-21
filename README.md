# aws_sdk_examples
AWS SDK examples that work with EC2 instances

Use SDK's to do the following commands (or equivalent):
```bash
# list all instances
aws ec2 describe-instances


# list only instances per a filter
aws ec2 describe-instances --filters "Name=tag:Type, Values=StudentWorkstation"

# start and stop instances
aws ec2 start-instances --instance-ids "string-id-1" "string-id-2"
aws ec2 stop-instances --instance-ids "string-id-1" "string-id-2"
```
