import boto3

# Initialize AWS IAM client
iam = boto3.client('iam')

def list_iam_roles():
    try:
        response = iam.list_roles()
        for role in response['Roles']:
            print(f"Role Name: {role['RoleName']}, ARN: {role['Arn']}, Created On: {role['CreateDate']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_iam_roles()
