import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_security_groups():
    try:
        response = ec2.describe_security_groups()
        for sg in response['SecurityGroups']:
            print(f"Group Name: {sg['GroupName']}, Group ID: {sg['GroupId']}, Description: {sg['Description']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_security_groups()
