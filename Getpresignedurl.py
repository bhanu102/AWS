import logging
import boto3
from botocore.exceptions import ClientError
import json


def create_presigned_url(bucket_name, object_name, expiration):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=int(expiration))
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

def lambda_handler(event, context):
    logging.info(f"Recieved Event: {json.dumps(event, indent=4)}")     
    event_body = json.loads(event.get("body", json.dumps({})))
    
    bucket_name = event_body.get("bucket_name")
    object_name = event_body.get("object_name")
    expiration_time = event_body.get("expiration_time", 3600)

    if not bucket_name or not object_name:
        response = {
            "error_message":"bucket_name, object_name fields are must  in body and expiration_time is optional."
        }
    else:
        pre_signed_url = create_presigned_url(bucket_name, object_name, expiration_time)    

        response = {
            "pre_signed_url":pre_signed_url,
            "valid_for": f"next {expiration_time} seconds",
            "bucket_name": bucket_name,
            "object_name": object_name
        }

    return {
                "statusCode":200,  
                "headers":{"Access-Control-Allow-Origin": "*"}, 
                "body": json.dumps(response)
            }