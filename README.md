# Multi-Region Sales Data Streaming Solution
## Description
This is a cloud-based data streaming solution for multi-region sales data.

## Architecture Diagram
![Image of Architecture design](https://github.com/lloydtawanda/RegionSalesDataStreaming/blob/master/architecture.png?raw=true)

## Prerequisites
1. Access to Amazon Web Services (AWS) Cloud Computing Services.
2. Access to Amazon Kinesis Data Streams Service.
3. Access to AWS Lambda Sevice.
4. Access to Amazon Scalable Storage Service (S3).
5. Access to Amazon QuickSight or Amazon DynamoDB (optional).

## Limitations (AWS Lambda)
1. Function memory allocation: 128 MB to 3,008 MB, in 64 MB increments.
2. Function timeout: 900 seconds (15 minutes)
3. Function environment variables: 4 KB
4. Function resource-based policy: 20 KB
5. Function layers: 5 layers
6. Invocation frequency (requests per second):
   - 10 x concurrent executions limit (synchronous – all sources)
   - 10 x concurrent executions limit (asynchronous – non-AWS sources)
   - Unlimited (asynchronous – AWS service sources)
7. Invocation payload (request and response): 
   - 6 MB (synchronous)
   - 256 KB (asynchronous)
8. Deployment package size: 
   - 50 MB (zipped, for direct upload)
   - 250 MB (unzipped, including layers)
   - 3 MB (console editor)
9. Test events (console editor): 10
10. /tmp directory storage: 512 MB
11. File descriptors: 1,024
12. Execution processes/threads: 1,024

## Assumptions
1. 
