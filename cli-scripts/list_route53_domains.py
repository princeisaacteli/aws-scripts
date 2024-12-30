import boto3

# Initialize AWS Route53 client
route53 = boto3.client('route53')

def list_route53_domains():
    try:
        response = route53.list_hosted_zones()
        for zone in response['HostedZones']:
            print(f"Zone Name: {zone['Name']}, Zone ID: {zone['Id']}, Private: {zone['Config']['PrivateZone']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_route53_domains()
