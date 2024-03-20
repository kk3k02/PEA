class ReadFile:

    # Konstruktor definiuje nazwę pliku, liczbę wierzchołków oraz tablicę wag krawędzi grafu
    def __init__(self, filePath):
        self.filePath = filePath
        self.num_ver = 0
        self.cost_list = []

    # Otwieranie pliku
    def openFile(self):
        file = open(self.filePath, "r")
        return file

    # Wczytywanie danych
    def readData(self):
        file = self.openFile()
        self.num_ver = int(file.readline())

        for i in range(self.num_ver):
            distance = [int(x) for x in file.readline().split()]
            self.cost_list.append(distance)

        # Zamykanie pliku
        file.close()

        # Zwracanie danych w formie listy 2x2
        return self.cost_list
