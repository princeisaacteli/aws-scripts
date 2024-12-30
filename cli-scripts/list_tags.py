import boto3

# Initialize AWS Resource Groups Tagging API client
tag_client = boto3.client('resourcegroupstaggingapi')

def list_tags():
    try:
        response = tag_client.get_resources()
        for resource in response['ResourceTagMappingList']:
            print(f"Resource ARN: {resource['ResourceARN']}")
            for tag in resource['Tags']:
                print(f"  {tag['Key']}: {tag['Value']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_tags()
