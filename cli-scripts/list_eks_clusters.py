import boto3

# Initialize AWS EKS client
eks = boto3.client('eks')

def list_eks_clusters():
    try:
        response = eks.list_clusters()
        for cluster in response['clusters']:
            print(f"EKS Cluster: {cluster}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_eks_clusters()
