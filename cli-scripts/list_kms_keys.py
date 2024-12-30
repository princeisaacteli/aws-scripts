import boto3

# Initialize AWS KMS client
kms = boto3.client('kms')

def list_kms_keys():
    try:
        response = kms.list_keys()
        for key in response['Keys']:
            key_metadata = kms.describe_key(KeyId=key['KeyId'])
            print(f"Key ID: {key['KeyId']}, Description: {key_metadata['KeyMetadata'].get('Description', 'No Description')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_kms_keys()
