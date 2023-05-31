import requests
import json

url = "http://127.0.0.1:5000/"

data = {"Leadsheet": "leadsheet2.csv",
        "jobName" : "job1"}

r = requests.post(url=url, data=json.dumps(data),headers={"Content-Type": "application/json"})
print(r)
print(r.json)
print("Message Sent")