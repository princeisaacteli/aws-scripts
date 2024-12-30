import boto3

# Initialize AWS SQS client
sqs = boto3.client('sqs')

def list_sqs_queues():
    try:
        response = sqs.list_queues()
        if 'QueueUrls' in response:
            for queue_url in response['QueueUrls']:
                print(f"Queue URL: {queue_url}")
        else:
            print("No SQS queues found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_sqs_queues()
