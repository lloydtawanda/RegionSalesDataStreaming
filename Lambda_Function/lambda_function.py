import json
import boto3


GLUE_ETL_JOB_NAME = "<Enter the name of the Glue ETL Job name>"

def lambda_handler(event, context):
    """
    Method is used to invoke Glue ETL job.
    
    Args:
        event (dict): Data passed from Amazon S3 PUT event.
        context (LambdaContext): Contains methods and properties
        that provide information about the invocation, function, and execution environment. 
        
    Returns:
        dict: Response from triggering Glue ETL Job.
    """
    client = boto3.client('glue')
    response = client.start_job_run(
        JobName=GLUE_ETL_JOB_NAME)
    return response
