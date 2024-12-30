import boto3

# Initialize AWS Lambda client
lambda_client = boto3.client('lambda')

def list_lambda_functions():
    try:
        response = lambda_client.list_functions()
        for function in response['Functions']:
            print(f"Function Name: {function['FunctionName']}, Runtime: {function['Runtime']}, Last Modified: {function['LastModified']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_lambda_functions()
