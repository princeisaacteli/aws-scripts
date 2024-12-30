import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_nat_gateways():
    try:
        response = ec2.describe_nat_gateways()
        for nat in response['NatGateways']:
            print(f"NAT Gateway ID: {nat['NatGatewayId']}, State: {nat['State']}, VPC: {nat['VpcId']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_nat_gateways()
