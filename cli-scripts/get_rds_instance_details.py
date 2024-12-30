import boto3

# Initialize AWS RDS client
rds = boto3.client('rds')

def get_rds_instance_details(db_instance_identifier):
    try:
        response = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
        for db in response['DBInstances']:
            print(f"DB Identifier: {db['DBInstanceIdentifier']}, Status: {db['DBInstanceStatus']}, Endpoint: {db['Endpoint']['Address']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    db_instance_identifier = 'my-db-instance'
    get_rds_instance_details(db_instance_identifier)
