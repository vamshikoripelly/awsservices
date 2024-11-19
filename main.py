#  import boto3
#
# Initialize the S3 client
# s3_client = boto3.client('s3')
#
#
# def csv_function(event,context):
#     bucket_name = event['bucket_name']
#     file_key = event['file_key']
#     try:
#         # Get the file from the S3 bucket
#         response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
#
#         # Read the file content (in this case, text)
#         file_content = response['Body'].read().decode('utf-8')
#
#         # Print the content (you can process it further as needed)
#         print(file_content)
#
#     except Exception as e:
#         print(f"Error reading file from S3: {e}")
#
