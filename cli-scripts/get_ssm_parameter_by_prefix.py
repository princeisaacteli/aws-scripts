import boto3

# Initialize AWS SSM client
ssm = boto3.client('ssm')

def get_parameters_by_prefix(prefix):
    try:
        response = ssm.get_parameters_by_path(
            Path=prefix,
            Recursive=True,
            WithDecryption=True
        )
        for param in response['Parameters']:
            print(f"Name: {param['Name']}, Value: {param['Value']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    prefix = '/application/config/'
    get_parameters_by_prefix(prefix)
