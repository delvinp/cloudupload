# Upload to cloud

This is an upload to cloud package. This will help to upload directory and subdirectory to AWS or GCS. Executable file will be there in the dist folder.

Code to upload directory to AWS:
--------------------------------
  from cloud_upload import upload_to_aws
  upload_to_aws.upload_directory(directory_path, destination_bucket_name, destination_blob_name, gcs_credentials, allowed_extensions)

Code to upload directory to GCS:
--------------------------------
  from cloud_upload import upload_to_gcs
  upload_to_gcs.upload_directory(directory_path, destination_bucket_name, aws_credentials, allowed_extensions)




In these functions,

directory_path is the local path of directory to be uploaded. Eg.: directory_path = "path/to/directory"

destination_bucket_name is the cloud bucket name to be uploaded. Eg.: destination_bucket_name = "destination_bucket_name"

gcs_credentials is the credentials which are obtained from gcs as json. Eg.: gcs_credentials = { "type": "type", "project_id": "project_id", "private_key_id": "private_key_id", "private_key":"private_key","client_email": "client_email", "client_id": "client_id", "auth_uri": "auth_uri", "token_uri": "token_uri", "auth_provider_x509_cert_url": "auth_provider_x509_cert_url", "client_x509_cert_url": "client_x509_cert_url"}

aws_credentials is the credentials which are obtained from aws.  Eg.: aws_credentials = { "aws_access_key_id": "aws_access_key_id", "aws_secret_access_key": "aws_secret_access_key", "region_name": "region_name" }

allowed_extensions is not mandatory. If we need to add only some extensions that have to be uploaded, please specify a list of extensions there. Eg.: allowed_extensions = ["png", "jpg"]
