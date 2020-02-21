import boto3

ec2client = boto3.client('ec2')

studentWorkstationFilter = [{ 
    'Name': 'tag:Type',
    'Values': ['StudentWorkstation'] 
}]

response = ec2client.describe_instances(Filters = studentWorkstationFilter)

instanceIds = []
print("--- EC2 instnace IDs ---")
print('-' * 40)
reservations = response['Reservations']
for reservation in reservations:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
        instanceIds.append(instance['InstanceId'])
        
ec2client.stop_instances(InstanceIds = instanceIds)
print()
