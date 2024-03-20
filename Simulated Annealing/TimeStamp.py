import time


class TimeStamp:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        exec_time = self.end_time - self.start_time
        return exec_time
