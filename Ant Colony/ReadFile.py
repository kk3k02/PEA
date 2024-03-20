import sys


class ReadFile:
    g = []
    vertices = 0

    def __init__(self, filename):
        self.loadFromFile(filename)

    def loadFromFile(self, filename):
        ver = ""

        for char in filename:
            if char.isdigit():
                ver += char

        self.vertices = int(ver)

        self.g = []
        file = open(filename, "r")
        edges_number = []

        lastThreeCharacters = filename[-3] + filename[-2] + filename[-1]

        if lastThreeCharacters == "xml":
            line = file.readline()
            num = []

            while line != "  <graph>\n":  # skip to edge declaration part of file
                line = file.readline()

            # inserts distance values for graph
            while line != "  </graph>\n":
                distances = []  # array of distances for one vertex
                # inserts distance values for one vertex
                while line != "    </vertex>\n":
                    # checks if line has declaration part
                    if line[6:17] == "<edge cost=":
                        current_number = ""
                        costBase = float(line[18:35])  # edge cost - base
                        costPower = float(line[37:39])  # edge cost power

                        for char in line[41:45]:
                            if char.isdigit():
                                current_number += char

                        num.append(int(current_number))

                        # cost is written in scientific notation
                        cost = costBase * (10 ** costPower)
                        distances.append(cost)

                    line = file.readline()

                # append row to matrix
                self.g.append(distances)

                # skip to next vertex declaration
                line = file.readline()

            sub_list = [num[0]]

            for i in num[1:]:
                if i < sub_list[-1]:
                    edges_number.append(sub_list)
                    sub_list = [i]
                else:
                    sub_list.append(i)
            edges_number.append(sub_list)

            for i in range(self.vertices):
                for j in range(self.vertices):
                    if j not in edges_number[i]:
                        self.g[i].insert(j, sys.float_info.max)

        elif lastThreeCharacters == "txt":
            self.vertices = int(file.readline())

            for i in range(self.vertices):
                distance = [int(x) for x in file.readline().split()]
                self.g.append(distance)

        # Zamykanie pliku
        file.close()