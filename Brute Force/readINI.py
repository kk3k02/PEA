class ReadINI:

    def __init__(self, filePath):
        self.filePath = filePath
        self.fileNames = []
        self.repeats = []

    def readData(self):
        with open(self.filePath, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    file_name = parts[0]
                    repeat = int(parts[1])
                    self.fileNames.append(file_name)
                    self.repeats.append(repeat)

        return self.fileNames, self.repeats
