import boto3

# Initialize AWS RDS client
rds = boto3.client('rds')

def list_rds_instances():
    try:
        response = rds.describe_db_instances()
        for db in response['DBInstances']:
            print(f"DB Identifier: {db['DBInstanceIdentifier']}, Status: {db['DBInstanceStatus']}, Endpoint: {db['Endpoint']['Address']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_rds_instances()
