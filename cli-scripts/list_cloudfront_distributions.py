import boto3

# Initialize AWS CloudFront client
cloudfront = boto3.client('cloudfront')

def list_cloudfront_distributions():
    try:
        response = cloudfront.list_distributions()
        if 'DistributionList' in response and 'Items' in response['DistributionList']:
            for distribution in response['DistributionList']['Items']:
                print(f"ID: {distribution['Id']}, Domain: {distribution['DomainName']}, Status: {distribution['Status']}")
        else:
            print("No distributions found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_cloudfront_distributions()
