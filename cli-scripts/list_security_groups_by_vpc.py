import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_security_groups_by_vpc(vpc_id):
    try:
        response = ec2.describe_security_groups(
            Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
        )
        for sg in response['SecurityGroups']:
            print(f"Group Name: {sg['GroupName']}, Group ID: {sg['GroupId']}, Description: {sg['Description']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    vpc_id = 'vpc-0123456789abcdef0'
    list_security_groups_by_vpc(vpc_id)
