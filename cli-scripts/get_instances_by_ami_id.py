import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def get_instances_by_ami_id(ami_id):
    try:
        response = ec2.describe_instances(
            Filters=[{'Name': 'image-id', 'Values': [ami_id]}]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}, AMI: {ami_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    get_instances_by_ami_id('ami-0123456789abcdef0')
