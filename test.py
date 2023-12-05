import boto3


s3 = boto3.resource('s3') # creating a s3 resource

bucket = s3.Bucket('dasun-bucket')

object_summary_iterator = bucket.objects.all()

for obj in object_summary_iterator:
    print(obj.key)