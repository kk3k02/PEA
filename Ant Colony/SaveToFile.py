import csv


class SaveToFile:
    def __init__(self, result_path, file_name, ver, cost, path, schema, alpha, beta, rho, num_iter, q, error_level, times):
        self.result_path = result_path
        self.file_name = file_name
        self.ver = ver
        self.cost = cost
        self.path = path
        self.schema = schema
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.num_iter = num_iter
        self.q = q
        self.error_level = error_level
        self.times = times

    def save(self):
        with open(self.result_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.file_name, self.ver, self.cost, self.path])
            writer.writerow([self.schema, self.alpha, self.beta, self.rho, self.num_iter, self.q])
            writer.writerow([self.error_level])
            writer.writerows([[str(time)] for time in self.times])