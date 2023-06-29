import time

class MockJob():

    def run(self, data):
        print("Starting job...")
        time.sleep(10)
        print(data + ' lmao')
        print("Job done!")