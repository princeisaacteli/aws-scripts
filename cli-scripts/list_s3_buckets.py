import boto3

# Initialize AWS S3 client
s3 = boto3.client('s3')

def list_s3_buckets():
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            print(f"Bucket Name: {bucket['Name']}, Created On: {bucket['CreationDate']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_s3_buckets()
