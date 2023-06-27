import boto3
import uuid

def send_sqs_message(queue_url, message_body,message_group_id):
    # Create an SQS client
    sqs = boto3.client('sqs')

    # Generate a unique message deduplication ID
    deduplication_id = str(uuid.uuid4())

    # Send a message to the specified queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body,
        MessageGroupId=message_group_id,
        MessageDeduplicationId=deduplication_id
    )

    # Check if the message was sent successfully
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f'Message sent successfully to message group: {message_group_id}.')
    else:
        print('Failed to send message.')

if __name__ == "__main__":
    # Example usage
    queue_url = "https://sqs.us-east-1.amazonaws.com/355974637362/AISNIPS-testCCQ.fifo"
    message = 'Hello, scraper!'
    message_group_id = 'scraper'
    send_sqs_message(queue_url, message, message_group_id)
    message = 'Hello, worker!'
    message_group_id = 'worker'
    send_sqs_message(queue_url, message, message_group_id)
