import glob
import os
from google.cloud import storage
from google.oauth2 import service_account


def upload_directory(directory_path, destination_bucket_name, destination_blob_name, gcs_credentials, allowed_extensions=None):
    try:
        credentials = service_account.Credentials.from_service_account_info(gcs_credentials)
        client = storage.Client(project=gcs_credentials['project_id'], credentials=credentials)
        rel_paths = glob.glob(directory_path + '/**', recursive=True)
        bucket = client.get_bucket(destination_bucket_name)
        for local_file in rel_paths:
            remote_path = f'{destination_blob_name}/{"/".join(local_file.split(os.sep)[1:])}'
            if os.path.isfile(local_file):
                upload_flag = True
                if allowed_extensions is not None:
                    if os.path.splitext(local_file)[1][1:] not in allowed_extensions:
                        upload_flag = False
                if upload_flag:
                    blob = bucket.blob(remote_path)
                    blob.upload_from_filename(local_file)
        return True
    except Exception as ex:
        print(ex)
        return False
