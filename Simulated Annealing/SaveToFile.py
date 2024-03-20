import csv


class SaveToFile:
    def __init__(self, path, file_name, schema, repeats, iterations, init_temp, error_level, times):
        self.path = path
        self.file_name = file_name
        self.schema = schema
        self.repeats = repeats
        self.iterations = iterations
        self.init_temp = init_temp
        self.error_level = error_level
        self.times = times

    def save(self):
        with open(self.path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.file_name, self.schema, self.repeats, self.iterations, self.init_temp, self.error_level])
            writer.writerows([[str(time)] for time in self.times])
