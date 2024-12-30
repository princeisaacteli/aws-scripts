import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def stop_instances_by_tag(tag_key, tag_value):
    try:
        response = ec2.describe_instances(
            Filters=[
                {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
                {'Name': 'instance-state-name', 'Values': ['running']}
            ]
        )
        instance_ids = [
            instance['InstanceId']
            for reservation in response['Reservations']
            for instance in reservation['Instances']
        ]
        
        if instance_ids:
            ec2.stop_instances(InstanceIds=instance_ids)
            print(f"Stopping instances: {', '.join(instance_ids)}")
        else:
            print("No running instances found with the given tag.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    stop_instances_by_tag('Environment', 'Dev')
