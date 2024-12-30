import boto3

# Initialize AWS SSM client
ssm = boto3.client('ssm')

def get_ssm_parameter_values(parameter_names):
    try:
        response = ssm.get_parameters(
            Names=parameter_names,
            WithDecryption=True
        )
        for param in response['Parameters']:
            print(f"Name: {param['Name']}, Value: {param['Value']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Add your parameter names here
    parameter_names = ['/app/db/password', '/app/api/key']
    get_ssm_parameter_values(parameter_names)
