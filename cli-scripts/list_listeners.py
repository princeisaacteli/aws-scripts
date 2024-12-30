import boto3

# Initialize AWS ELBv2 client
elbv2 = boto3.client('elbv2')

def list_listeners():
    try:
        lbs = elbv2.describe_load_balancers()['LoadBalancers']
        for lb in lbs:
            lb_arn = lb['LoadBalancerArn']
            listeners = elbv2.describe_listeners(LoadBalancerArn=lb_arn)
            for listener in listeners['Listeners']:
                print(f"Load Balancer: {lb['LoadBalancerName']}, Listener ARN: {listener['ListenerArn']}, Port: {listener['Port']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_listeners()
