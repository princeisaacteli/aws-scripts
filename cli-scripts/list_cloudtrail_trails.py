import boto3

# Initialize AWS CloudTrail client
cloudtrail = boto3.client('cloudtrail')

def list_cloudtrail_trails():
    try:
        response = cloudtrail.describe_trails()
        for trail in response['trailList']:
            print(f"Trail Name: {trail['Name']}, S3 Bucket: {trail['S3BucketName']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_cloudtrail_trails()
