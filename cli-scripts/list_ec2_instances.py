import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_ec2_instances():
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Type: {instance['InstanceType']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_ec2_instances()
