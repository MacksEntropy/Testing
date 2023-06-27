import time

class MockJob():

    def run(self):
        print("Starting job...")
        time.sleep(10)
        print("Job done!")