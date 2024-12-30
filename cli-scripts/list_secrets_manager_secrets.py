import boto3

# Initialize AWS Secrets Manager client
secretsmanager = boto3.client('secretsmanager')

def list_secrets():
    try:
        response = secretsmanager.list_secrets()
        for secret in response['SecretList']:
            print(f"Secret Name: {secret['Name']}, ARN: {secret['ARN']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_secrets()
