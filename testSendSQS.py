import boto3
import ast

sqs = boto3.client('sqs')

response = sqs.list_queues()

devQURL = response['QueueUrls'][1]

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=devQURL,
    DelaySeconds=10,
    #Message body must be str
    MessageBody=(
        str({'Leadsheet': 'leadsheet.csv',
        'jobName' : 'job1'})
    )
)

print('SENT: ', response['MessageId'])