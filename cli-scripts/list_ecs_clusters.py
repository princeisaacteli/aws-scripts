import boto3

# Initialize AWS ECS client
ecs = boto3.client('ecs')

def list_ecs_clusters():
    try:
        response = ecs.list_clusters()
        for cluster in response['clusterArns']:
            print(f"Cluster ARN: {cluster}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_ecs_clusters()
