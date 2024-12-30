import boto3

# Initialize AWS Auto Scaling client
autoscaling = boto3.client('autoscaling')

def set_asg_to_zero(asg_name):
    try:
        autoscaling.update_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            DesiredCapacity=0,
            MinSize=0,
            MaxSize=0
        )
        print(f"Set Auto Scaling Group '{asg_name}' capacity to zero.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    set_asg_to_zero('my-auto-scaling-group')
