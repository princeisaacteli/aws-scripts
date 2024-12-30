import boto3

# Initialize AWS ElastiCache client
elasticache = boto3.client('elasticache')

def list_elasticache_clusters():
    try:
        response = elasticache.describe_cache_clusters()
        for cluster in response['CacheClusters']:
            print(f"Cluster ID: {cluster['CacheClusterId']}, Status: {cluster['CacheClusterStatus']}, Engine: {cluster['Engine']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_elasticache_clusters()
