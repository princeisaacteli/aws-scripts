import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_vpcs():
    try:
        response = ec2.describe_vpcs()
        for vpc in response['Vpcs']:
            print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}, State: {vpc['State']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_vpcs()
