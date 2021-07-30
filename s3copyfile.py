import boto3

s3 = boto3.resource('s3')
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    copy_source = {
        'Bucket': bucket,
        'Key': key
        }
    try:
        destbucket = s3.Bucket('s3writedata')
        destbucket.copy(copy_source, key)
        print('{} transferred to destination bucket'.format(key))

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. '.format(key, bucket))
        raise e