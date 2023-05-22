import boto3
import ast

sqs = boto3.client('sqs',  region_name='us-east-1',)

response = sqs.list_queues()

devQURL = response['QueueUrls'][1]

# Receive message from SQS queue
lmao = sqs.receive_message(QueueUrl=devQURL)

message = lmao['Messages'][0]
MessageBody = message['Body']
# print('Message Body is ', type(MessageBody) ,MessageBody)
dictBody = ast.literal_eval(MessageBody)
print('Dict Body is ', type(dictBody) ,dictBody['Leadsheet'])


# Delete received message from queue
receipt_handle = message['ReceiptHandle']
sqs.delete_message(
    QueueUrl=devQURL,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)