import boto3

from mockJob import MockJob

def receive_sqs_message(queue_url, message_group_id):

    sqs = boto3.client('sqs', region_name='us-east-1')

    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,              
        WaitTimeSeconds=10,                 # Wait time for a message to become available (optional)
        VisibilityTimeout=60,               # Time the message is hidden from subsequent retrieve requests (optional)
        AttributeNames=['MessageGroupId'],  # Include MessageGroupId attribute to ensure FIFO ordering
    )

    if 'Messages' in response:
        message = response['Messages'][0]  # Extract the first message from the response
        receipt_handle = message['ReceiptHandle']  # Retrieve the receipt handle to delete the message later

        # Check if the received message has the expected MessageGroupId
        if message['Attributes']['MessageGroupId'] == message_group_id:
            # Process the received message
            print('Received message:', message['Body'])

            # Delete the message from the queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )


            m = MockJob()
            m.run()

        else:
            print(f'No messages in queue from group id: {message_group_id}')
    else:
        print('No messages in the queue.')


if __name__ == "__main__":
    # Example usage
    queue_url = "https://sqs.us-east-1.amazonaws.com/355974637362/AISNIPS-testCCQ.fifo"
    message_group_id = 'scraper'
    print(f"Recieving message from group id: {message_group_id}")
    receive_sqs_message(queue_url,message_group_id)