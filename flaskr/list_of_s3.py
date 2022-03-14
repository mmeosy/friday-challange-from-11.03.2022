import boto3

client = boto3.client("s3")


def list_objects(bucket_name):
    response = client.list_objects(Bucket = bucket_name)
    print(response["Contents"])
    
    
    
