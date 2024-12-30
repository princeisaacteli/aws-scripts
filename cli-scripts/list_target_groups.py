import boto3

# Initialize AWS Elastic Load Balancing (ELB) client
elbv2 = boto3.client('elbv2')

def list_target_groups():
    try:
        response = elbv2.describe_target_groups()
        for tg in response['TargetGroups']:
            print(f"Name: {tg['TargetGroupName']}, ARN: {tg['TargetGroupArn']}, Protocol: {tg['Protocol']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_target_groups()
