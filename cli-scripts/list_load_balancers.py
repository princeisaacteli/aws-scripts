import boto3

# Initialize AWS ELBv2 client
elbv2 = boto3.client('elbv2')

def list_load_balancers():
    try:
        response = elbv2.describe_load_balancers()
        for lb in response['LoadBalancers']:
            print(f"Name: {lb['LoadBalancerName']}, ARN: {lb['LoadBalancerArn']}, DNS: {lb['DNSName']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_load_balancers()
