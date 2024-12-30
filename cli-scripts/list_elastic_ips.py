import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_elastic_ips():
    try:
        response = ec2.describe_addresses()
        for address in response['Addresses']:
            print(f"Public IP: {address['PublicIp']}, Instance ID: {address.get('InstanceId', 'Not Attached')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_elastic_ips()
