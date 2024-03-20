import readFile
import tsp
import timeStamp
import saveToFile
import readINI


def main():
    time = timeStamp.TimeStamp()
    times = []  # Wyniki pomiarów czasu
    cost = 0  # Koszt wybranej ścieżki
    path = []  # Najkrótsza ścieżka

    # Wczytywanie danych o liczbie powtórzeń i nazwach plików
    reader = readINI.ReadINI("test.INI")
    filePaths, repeat = reader.readData()

    # Testowanie algorytmu
    for i in range(len(repeat)):
        # Wczytanie macierzy sąsiedztwa
        file = readFile.ReadFile(filePaths[i])
        data = file.readData()
        algorithm = tsp.Tsp(file.num_ver, data)

        for j in range(repeat[i]):
            # Wykonanie algorytmu
            time.start()
            cost, path = algorithm.start()
            exec_time = time.end()
            times.append(exec_time)
            print("Time: ", exec_time, " [s]")
            print(int(((i/len(repeat))*100)), ".", int(((j/(repeat[i]))*100)), "%")

        # Zapisywanie do pliku wynikowego
        saveFile = saveToFile.SaveToFile(filePaths[i], repeat[i], cost, path, times)
        saveFile.save()
        print("\n")

        times = []  # Czyszczenie tablicy z czasami pomiarów


# Start programu
if __name__ == "__main__":
    main()
