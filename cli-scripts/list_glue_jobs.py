import boto3

# Initialize AWS Glue client
glue = boto3.client('glue')

def list_glue_jobs():
    try:
        response = glue.list_jobs()
        for job in response['JobNames']:
            print(f"Glue Job: {job}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_glue_jobs()
