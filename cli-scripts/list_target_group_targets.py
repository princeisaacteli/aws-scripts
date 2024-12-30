import boto3

# Initialize AWS ELBv2 client
elbv2 = boto3.client('elbv2')

def list_target_group_targets(target_group_arn):
    try:
        response = elbv2.describe_target_health(TargetGroupArn=target_group_arn)
        for target in response['TargetHealthDescriptions']:
            print(f"Target ID: {target['Target']['Id']}, State: {target['TargetHealth']['State']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    target_group_arn = 'arn:aws:elasticloadbalancing:region:account-id:targetgroup/name/id'
    list_target_group_targets(target_group_arn)
