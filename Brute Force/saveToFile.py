import csv


class SaveToFile:
    def __init__(self, fileName, repeats, cost, path, times):
        self.fileName = fileName
        self.repeats = repeats
        self.cost = cost
        self.path = path
        self.times = times

    def save(self):
        with open('br_TSP_output.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=' ')
            # Usuń cudzysłowy z ścieżki przed zapisem
            path_without_quotes = str(self.path).strip('"')
            # Usuń spacje w ścieżce przed zapisem
            path_without_spaces = path_without_quotes.replace(' ', '')
            writer.writerow([self.fileName, self.repeats, self.cost, path_without_spaces])
            for time in self.times:
                writer.writerow([time])
