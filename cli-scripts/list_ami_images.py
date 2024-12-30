import boto3

# Initialize AWS EC2 client
ec2 = boto3.client('ec2')

def list_ami_images():
    try:
        response = ec2.describe_images(Owners=['self'])
        for image in response['Images']:
            print(f"AMI ID: {image['ImageId']}, Name: {image['Name']}, State: {image['State']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_ami_images()
