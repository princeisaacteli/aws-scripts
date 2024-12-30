import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def get_instance_details(instance_id):
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Type: {instance['InstanceType']}")
                print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}, Private IP: {instance['PrivateIpAddress']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    instance_id = 'i-0123456789abcdef0'
    get_instance_details(instance_id)
