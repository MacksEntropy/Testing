import boto3
import uuid

class SQSUtils():

    def receive_sqs_message(self, queue_url : str, message_group_id : str) -> str | None:
        """
        Method for proccessing messages from a given SQS FIFO queue. 
        :param queue_url: AWS URL associated with SQS queue
        :param message_group_id: Message group ID string 
        
        Returns: 
            If a non-empty message is recieved, will return the message body as a string. 
            If an empty message is recieved, will return None. 
        """

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
                msg = message['Body']

                # Delete the message from the queue
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=receipt_handle
                )
                return msg
            else:
                print(f'No messages in queue from group id: {message_group_id}')
                return
        else:
            print('No messages in the queue.')
            return

    def send_sqs_message(self, queue_url: str, message_body: str, message_group_id: str) -> None:
        """
        Method for sending messages to a given SQS FIFO queue. 
        :param queue_url: AWS URL associated with SQS queue
        :param message_body: Message to be sent, must be a string. 
        :param message_group_id: Message group ID string 
        """

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