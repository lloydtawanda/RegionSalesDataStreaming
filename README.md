# Multi-Region Sales Data Streaming Solution
## Description
This is a cloud-based data streaming solution for multi-region sales data.

## Architecture Diagram
![Image of Architecture design](https://github.com/lloydtawanda/RegionSalesDataStreaming/blob/master/SalesStreamingArchitecture.png?raw=true)

## Prerequisites
1. Access to Amazon Web Services (AWS) Cloud Computing Services.
2. Access to Amazon Scalable Storage Service (S3).
   - Create S3 bucket called "Data" with the following folder structure:<br/>
   ![Image of S3 processed data bucket](https://github.com/lloydtawanda/RegionSalesDataStreaming/blob/master/s3_folder_structure.png)
   - Create S3 bucket called **_Streaming_** to store data streams
   - Create S3 sub-folders in **_Streaming_** bucket, called **_processed_** and **_backup_**
3. Access to AWS Glue Service
   - Create Glue Database called **_sales_db_** that points to S3 bucket prefix **_Streaming/processed_** 
   - Create Glue Table called **_sales_** and use the column names **_Sales data CSV files_** to define the table schema
   - Create Glue ETL Job called **_sales_etl_job_** and copy and paste script in _/PopulateKinesisFirehose/push_data.py_ into the job's script
4. Access to Amazon Kinesis Firehose Service.
   - Create Delivery stream using Kinesis Firehose
   - Configure **Source** to be _Direct PUT or other sources_
   - Set **Record transformation** to _Disabled_
   - Set **Record format conversion** to _Enabled_
   - Set **Output format** to _Apache Parquet_
   - Set **AWS Glue region** to _EU (Ireland)_
   - Set **AWS Glue database** to _sales_db
   - Set **AWS Glue table** to **_sales_**
   - Set **AWS Glue table version** to _Latest_
   - Set **Destination** to _Amazon S3_
   - Set **S3 bucket** to _Streaming_
   - Set **S3 prefix** to _processed_
   - Set **S3 error prefix** to _backup_
   - Set **Buffer size** to _128MB_
   - Set **Buffer interval** to _300s_
   - Set **S3 encryption** to _Disabled_
   - Set **Error logging** to _Enabled_
   - Set **Tags** (Optional)
   - Create IAM role with access S3 bucket where data streams will be stored, and Glue and Kinesis service role access
   - Assign IAM role to delivery stream
5. Access to AWS Lambda Sevice.
   - Create Lambda function called **_invoke_glue_etl_**
   - Set **Runtime** to Python 3.7 
   - Assign IAM role with access to Lambda Invoke Service and Glue Service access
   - Assign S3 trigger from **_Streaming_** bucket put event
   - Copy and paste code in _/Lambda_Function/lambda_function.py_ to the Lambda function script
6. Access to AWS Elastic Cloud Compute Service (EC2)
   - Start EC2 instance using AWS Linux AMI
   - Assign IAM role to access kinesis firehose service
   - Install or update python 3
   - Create python file called called **_push_data.py_**
   - Copy and paste code in _/PopulateKinesisFirehose/push_data.py_ to the file

## Limitations and Scaling Options
-  The python program used to preprocess data before pushing to kinesis firehose runs on a single EC2 instance, this requires a large instance when big data comes to perspective. Big data processing on a single-instance architecture will have implications on costs and processing, alternatively auto-scaling or distributed computing framework such as Apache Spark on EMR platform can be used for data preprocessing.

## Assumptions
1. Region Data is static and is stored in S3 location **_Data/Region_**
2. All sales data is stored in or pushed to EC2 instance as CSV files


