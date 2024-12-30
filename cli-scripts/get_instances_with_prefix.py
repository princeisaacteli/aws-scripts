import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def get_instances_with_prefix(prefix):
    try:
        response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Name', 'Values': [f'{prefix}*']}
            ]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Name: {prefix}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    prefix = 'web-server'
    get_instances_with_prefix(prefix)
