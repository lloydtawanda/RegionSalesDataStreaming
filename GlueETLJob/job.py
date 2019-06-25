import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# @constants
S3_BUCKET_RAW = 'Streaming'
S3_PREFIX_RAW = 'processed'
S3_BUCKET_DATA = 'Data'
S3_PREFIX_REGION = 'Region'
S3_PREFIX_SALES = 'Sales'
S3_PREFIX_OUTPUT = 'Output'
S3_PREFIX_ARCHIVE = 'Archive'

# @globals
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Contenate sales data
sales_df = spark.read.parquet("s3://{}/{}/*/*/*/*".format(S3_BUCKET_RAW, S3_PREFIX_RAW)


# Enrich sales data with region data
region_df = spark.read.format('com.databricks.spark.csv').option('delimiter', ',').load('s3://{}/{}/*.csv'.format(S3_BUCKET_DATA, S3_PREFIX_REGION))
enriched_df = sales_df.join(region_df, (sales_df.Region == region_df.Region))
# Archive enriched data in S3
enriched_dyf = DynamicFrame.fromDF(enriched_df, glueContext, "enriched_dyf")
datasink0 = glueContext.write_dynamic_frame.from_options(frame = enriched_dyf , connection_type = "s3", connection_options = {"path": "s3://{}/{}/".format(S3_BUCKET_DATA, S3_PREFIX_ARCHIVE), "partitionKeys": ["Region"]}, format = "parquet", transformation_ctx = "datasink0")


# Total sales amount per region and network and save as output 
total_sales_df = sales_df.groupBy("Region", "Network").agg({'Amount':'sum'})
# Save Total sales to output S3 folder
total_sales_dyf = DynamicFrame.fromDF(total_sales_df, glueContext, "total_sales_dyf")
datasink1 = glueContext.write_dynamic_frame.from_options(frame = total_sales_dyf , connection_type = "s3", connection_options = {"path": "s3://{}/{}/".format(S3_BUCKET_DATA, S3_PREFIX_OUTPUT),"partitionKeys": ["Region"]}, format = "parquet", transformation_ctx = "datasink1")


# Commit job
job.commit()
