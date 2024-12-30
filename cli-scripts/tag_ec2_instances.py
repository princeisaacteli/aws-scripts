import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def tag_instances(instance_ids, tag_key, tag_value):
    try:
        ec2.create_tags(
            Resources=instance_ids,
            Tags=[{'Key': tag_key, 'Value': tag_value}]
        )
        print(f"Tagged instances {', '.join(instance_ids)} with {tag_key}: {tag_value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    tag_instances(['i-0123456789abcdef0'], 'Environment', 'Production')
