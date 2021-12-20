import boto3
import os


def upload_directory(directory_path, destination_bucket_name, aws_credentials, allowed_extensions=None):
    try:
        session = boto3.Session(
            aws_access_key_id=aws_credentials['aws_access_key_id'],
            aws_secret_access_key=aws_credentials['aws_secret_access_key'],
            region_name=aws_credentials['region_name']
        )
        s3 = session.resource('s3')
        bucket = s3.Bucket(destination_bucket_name)

        for subdir, dirs, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(subdir, file)
                with open(full_path, 'rb') as data:
                    upload_flag = True
                    if allowed_extensions is not None:
                        if os.path.splitext(full_path)[1][1:] not in allowed_extensions:
                            upload_flag = False
                    if upload_flag:
                        key = full_path[len(directory_path) + 1:]
                        bucket.put_object(Key=key, Body=data)
        return True
    except Exception as ex:
        print(ex)
        return False
