import boto3
import time

from sqsUtils import SQSUtils
from mockJob import MockJob

if __name__ == "__main__":
    sqs = SQSUtils()
    m  = MockJob()
    message = "Aye"
    queue_url = "https://sqs.us-east-1.amazonaws.com/355974637362/AISNIPS-testCCQ.fifo"
    message_group_id = 'scraper'
    sqs.send_sqs_message(queue_url, message, message_group_id)
    print("waiting for msg...")
    time.sleep(30)
    msg = sqs.receive_sqs_message(queue_url, message_group_id)
    m.run(msg)
