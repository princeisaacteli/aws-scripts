import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_instances_by_state(state):
    try:
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': [state]}]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    state = 'running'  # Change to 'stopped' if needed
    list_instances_by_state(state)
