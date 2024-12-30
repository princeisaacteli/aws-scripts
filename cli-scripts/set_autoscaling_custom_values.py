import boto3

# Initialize AWS Auto Scaling client
autoscaling = boto3.client('autoscaling')

def set_asg_capacity(asg_name, min_size, max_size, desired_capacity):
    try:
        autoscaling.update_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            MinSize=min_size,
            MaxSize=max_size,
            DesiredCapacity=desired_capacity
        )
        print(f"Updated Auto Scaling Group '{asg_name}' to Min: {min_size}, Max: {max_size}, Desired: {desired_capacity}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    set_asg_capacity('my-auto-scaling-group', 1, 5, 3)
