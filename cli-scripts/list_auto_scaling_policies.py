import boto3

# Initialize AWS Auto Scaling client
autoscaling = boto3.client('autoscaling')

def list_auto_scaling_policies():
    try:
        response = autoscaling.describe_policies()
        for policy in response['ScalingPolicies']:
            print(f"Policy Name: {policy['PolicyName']}, ASG: {policy['AutoScalingGroupName']}, Adjustment Type: {policy['AdjustmentType']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_auto_scaling_policies()
