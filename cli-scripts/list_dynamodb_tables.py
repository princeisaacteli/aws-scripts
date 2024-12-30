import boto3

# Initialize AWS DynamoDB client
dynamodb = boto3.client('dynamodb')

def list_dynamodb_tables():
    try:
        response = dynamodb.list_tables()
        for table in response['TableNames']:
            print(f"Table: {table}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_dynamodb_tables()
