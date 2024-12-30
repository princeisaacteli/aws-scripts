import boto3

# Initialize AWS Elastic Load Balancing (ELB) client
elbv2 = boto3.client('elbv2')

def list_unhealthy_target_groups():
    try:
        target_groups = elbv2.describe_target_groups()['TargetGroups']
        for tg in target_groups:
            tg_arn = tg['TargetGroupArn']
            health_response = elbv2.describe_target_health(TargetGroupArn=tg_arn)
            for target in health_response['TargetHealthDescriptions']:
                if target['TargetHealth']['State'] != 'healthy':
                    print(f"Target Group: {tg['TargetGroupName']}, Target: {target['Target']['Id']}, State: {target['TargetHealth']['State']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_unhealthy_target_groups()
