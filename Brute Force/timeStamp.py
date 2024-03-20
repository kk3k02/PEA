import time


class TimeStamp:
    def __init__(self):
        self.startTime = 0  # Czas startowy
        self.endTime = 0  # Czas końcowy
        self.execTime = 0  # Czas działania algorytmu

    def start(self):
        self.startTime = time.time()

    def end(self):
        self.endTime = time.time()
        self.execTime = self.endTime - self.startTime
        return self.execTime
