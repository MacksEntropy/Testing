import boto3
import ast

sqs = boto3.client('sqs')

workerQURL = "https://sqs.us-east-1.amazonaws.com/355974637362/awseb-e-jma2h8x3mm-stack-AWSEBWorkerQueue-SSTqsqvsF9sf"

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=workerQURL,
    DelaySeconds=10,
    #Message body must be str
    MessageBody=(
        str({'Leadsheet': 'leadsheet.csv',
        'jobName' : 'job1'})
    )
)

print('SENT')