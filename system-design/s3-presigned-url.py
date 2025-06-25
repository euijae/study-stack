import boto3
from botocore.exceptions import ClientError
import uuid

def generate_presigned_upload_url():
    s3_client = boto3.client('s3')
    expiration = 3600

    try:
        response = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': 'euijae-image',
                'Key': 'output2.txt',
                'ContentType': 'application/octet-stream'
            },
            ExpiresIn = expiration
        )
    except ClientError as e:
        print(f"Error generating presigned URL: {e}")
        return None
    
    return { 'url': response }

result = generate_presigned_upload_url()
print("Upload URL:", result["url"])