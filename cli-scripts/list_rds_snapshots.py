import boto3

# Initialize AWS RDS client
rds = boto3.client('rds')

def list_rds_snapshots():
    try:
        response = rds.describe_db_snapshots()
        for snapshot in response['DBSnapshots']:
            print(f"Snapshot ID: {snapshot['DBSnapshotIdentifier']}, DB Instance: {snapshot['DBInstanceIdentifier']}, Status: {snapshot['Status']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_rds_snapshots()
