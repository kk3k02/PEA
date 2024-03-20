class ReadINI:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        file_names = []
        repeats = []
        results = []
        paths = []

        with open(self.file_path, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) >= 4:
                    file_name = parts[0]
                    repeat = int(parts[1])
                    result = int(parts[2])
                    path = [int(node.strip('[],')) for node in parts[3:]]

                    file_names.append(file_name)
                    repeats.append(repeat)
                    results.append(result)
                    paths.append(path)

        return file_names, repeats, results, paths
