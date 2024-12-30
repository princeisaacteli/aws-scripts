import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def get_instances_by_tag(tag_key, tag_value):
    try:
        response = ec2.describe_instances(
            Filters=[
                {'Name': f'tag:{tag_key}', 'Values': [tag_value]}
            ]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    tag_key = 'Environment'
    tag_value = 'Production'
    get_instances_by_tag(tag_key, tag_value)
