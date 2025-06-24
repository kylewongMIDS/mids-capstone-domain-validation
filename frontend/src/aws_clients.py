import boto3
import uuid
# from sagemaker.sklearn.model import SKLearnModel


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
    
    unique_file_id = str(uuid.uuid4())
    bucket_name = f'streamlit-processing-input/{unique_file_id}'  # Your bucket name (not ARN)
    s3_key = f"{unique_file_id}.csv"  # The object key in the bucket
    
    # Upload the CSV file content to S3
    # If csv_file is a Streamlit uploaded file, use csv_file.getvalue()
    file_content = csv_file.getvalue() if hasattr(csv_file, 'getvalue') else csv_file.read()
    
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)
    
    return unique_file_id


def retrieve_csv_from_s3(file_id):
    s3 = boto3.client('s3')
    bucket_name = f'streamlit-processing-input/{file_id}'
    s3_key = f'{file_id}.csv'
    file_content = s3.get_object(Bucket=bucket_name, Key=s3_key)
    return s3_key


# def batch_transformation_job(model_name, input_file_id):
#     model = SKLearnModel(
#         model_data=f's3://capstonedata05212025/{model_name}/model.tar.gz',
#         role='arn:aws:iam::857128573675:role/service-role/AmazonSageMaker-ExecutionRole-20250527T214532',
#         entry_point='inference.py',
#         framework_version='0.23-1',
#         py_version='py3'
#     )

#     transformer = model.transformer(
#         instance_count = 1,
#         instance_type='ml.m5.large',
#         output_path=f's3://streamlit-processing-output/{input_file_id}',
#         assemble_with='Line',
#         accept='csv'
#     )
    
#     transformer.transform(
#         data=f's3://streamlit-processing-input/{input_file_id}',
#         content_type='csv',
#         split_type='Line'
#     )
    
#     transformer.wait()