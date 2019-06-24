 
import json
import boto3
import random
import datetime
import time
import glob
import pandas as pd

GLUE_ETL_JOB_NAME = "<Enter the name of the Glue ETL Job name>"
SALES_DATA_PATH = "<Enter the path for the sales data (csv) files>"


def getRecords(path):
    """
    Method is used to get data for all CSV files in the path.

    Args:
        path (string) : The path for the CSV files.

    Returns:
        list: A list of dictionaries with file data.
    """
    sales_data_files = [ file_name for file_name in glob.glob(f"{path}*.csv") ]
    dataframes = [ pd.read_csv(file_name) for file_name in sales_data_files ]
    dataframe = pd.concat(dataframes, ignore_index=True)
    return [ {'Data':json.dumps(record)} for record in dataframe.to_dict('records') ]


if __name__ == "__main__":
    
    firehose = boto3.client('firehose')
    records = getRecords(path=SALES_DATA_PATH)
    response = firehose.put_record_batch(
            DeliveryStreamName=GLUE_ETL_JOB_NAME,
            Records=records)

    print("Batch Put Record Response: \n{}".format(response))



