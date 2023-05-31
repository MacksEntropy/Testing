import boto3
import ast

sqs = boto3.client('sqs')

# response = sqs.list_queues()

# devQURL = response['QueueUrls'][1]

workerQURL = "https://sqs.us-east-1.amazonaws.com/355974637362/aisnips-webapi-worker-dev-queue"

print(sqs.attributes(QueueUrl=workerQURL))

# Receive message from SQS queue
# testMessage = sqs.receive_message(QueueUrl=workerQURL)

# message = testMessage['Messages'][0]
# # MessageBody = message['Body']
# # print('Message Body is ', type(MessageBody) ,MessageBody)
# # dictBody = ast.literal_eval(MessageBody)
# print(message)


# # Delete received message from queue
# receipt_handle = message['ReceiptHandle']
# sqs.delete_message(
#     QueueUrl=workerQURL,
#     ReceiptHandle=receipt_handle
# )
# print('Received and deleted message: %s' % message)