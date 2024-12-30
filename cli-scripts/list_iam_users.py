import boto3

# Initialize AWS IAM client
iam = boto3.client('iam')

def list_iam_users():
    try:
        response = iam.list_users()
        for user in response['Users']:
            print(f"User Name: {user['UserName']}, Created On: {user['CreateDate']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_iam_users()
