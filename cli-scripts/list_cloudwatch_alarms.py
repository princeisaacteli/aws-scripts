import boto3

# Initialize AWS CloudWatch client
cloudwatch = boto3.client('cloudwatch')

def list_cloudwatch_alarms():
    try:
        response = cloudwatch.describe_alarms()
        for alarm in response['MetricAlarms']:
            print(f"Alarm Name: {alarm['AlarmName']}, State: {alarm['StateValue']}, Metric: {alarm['MetricName']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_cloudwatch_alarms()
