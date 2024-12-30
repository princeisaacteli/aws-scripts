import boto3

# Initialize AWS Redshift client
redshift = boto3.client('redshift')

def list_redshift_clusters():
    try:
        response = redshift.describe_clusters()
        for cluster in response['Clusters']:
            print(f"Cluster ID: {cluster['ClusterIdentifier']}, Node Type: {cluster['NodeType']}, Status: {cluster['ClusterStatus']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_redshift_clusters()

