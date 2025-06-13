import boto3
import uuid

def write_csv_to_s3(csv_file):
    """
    Uploads a CSV file-like object to the S3 bucket 'streamlit-processing-input' 
    with a unique filename.

    Args:
        csv_file: A file-like object (e.g. BytesIO) containing CSV data.

    Returns:
        The S3 object key of the uploaded file.
    """
    # Create boto3 session and client
    s3 = boto3.client('s3')
    
    bucket_name = 'streamlit-processing-input'  # Your bucket name (not ARN)
    unique_file_id = str(uuid.uuid4())
    s3_key = f"{unique_file_id}.csv"  # The object key in the bucket
    
    # Upload the CSV file content to S3
    # If csv_file is a Streamlit uploaded file, use csv_file.getvalue()
    file_content = csv_file.getvalue() if hasattr(csv_file, 'getvalue') else csv_file.read()
    
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)
    
    return s3_key
