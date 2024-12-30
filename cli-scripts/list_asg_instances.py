import boto3

# Initialize AWS Auto Scaling client
autoscaling = boto3.client('autoscaling')

def list_asg_instances():
    try:
        response = autoscaling.describe_auto_scaling_groups()
        for asg in response['AutoScalingGroups']:
            print(f"ASG Name: {asg['AutoScalingGroupName']}, Instances:")
            for instance in asg['Instances']:
                print(f"  - Instance ID: {instance['InstanceId']}, State: {instance['LifecycleState']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_asg_instances()
