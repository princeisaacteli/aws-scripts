import boto3

# Initialize AWS CloudFormation client
cloudformation = boto3.client('cloudformation')

def list_cloudformation_stacks():
    try:
        response = cloudformation.describe_stacks()
        for stack in response['Stacks']:
            print(f"Stack Name: {stack['StackName']}, Status: {stack['StackStatus']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_cloudformation_stacks()
