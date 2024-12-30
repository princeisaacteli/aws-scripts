import boto3

# Initialize AWS S3 client
s3 = boto3.client('s3')

def list_s3_objects(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"Key: {obj['Key']}, Size: {obj['Size']} bytes, Last Modified: {obj['LastModified']}")
        else:
            print("No objects found in this bucket.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'
    list_s3_objects(bucket_name)
