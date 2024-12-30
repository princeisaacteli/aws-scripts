import boto3

# Initialize AWS Backup client
backup = boto3.client('backup')

def list_backup_vaults():
    try:
        response = backup.list_backup_vaults()
        for vault in response['BackupVaultList']:
            print(f"Vault Name: {vault['BackupVaultName']}, ARN: {vault['BackupVaultArn']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_backup_vaults()
