from ReadINI import ReadINI
from ReadFile import ReadFile
from TimeStamp import TimeStamp
from aco import ACO, Graph
from SaveToFile import SaveToFile


def main():
    # AC alg. settings
    alpha = 1.0  # Wpływ feromonów na wybór trasy
    beta = 2.0  # Wpływ widoczności na wybór trasy
    rho = 0.5  # Współczynnik parowania feromonów
    num_itr = 100  # Ilość iteracji algorytmu
    strategy = [0, 1, 2]  # Strategia aktualizacji feromonów (0 - CAS, 1 - QAS, 2 - DAS)
    q = 100  # Intensywność feromonów

    output = ["results/ACO_CAS.csv", "results/ACO_QAS.csv", "results/ACO_DAS.csv"]

    schemas = ["CAS", "QAS", "DAS"]

    iniPath = "test.INI"
    reader = ReadINI(iniPath)
    file_names, repeats, results, paths = reader.read_data()
    timestamp = TimeStamp()

    for i in range(len(file_names)):
        file = ReadFile(file_names[i])
        print("===================================================")
        print(file_names[i])
        print()

        for j in range(len(schemas)):
            result_times = []
            errors = 0.0

            print("Strategy: ", schemas[j])
            print("Alpha=", alpha, " Beta=", beta, " Rho=", rho, " Ants=", file.vertices)
            print("Best path:", paths[i])
            print("Best cost:", results[i])
            print()

            for k in range(repeats[i]):
                timestamp.start()
                aco = ACO(file.vertices, num_itr, alpha, beta, rho, q, strategy[j])
                graph = Graph(file.g, file.vertices)
                path, cost = aco.solve(graph)
                result = timestamp.end()
                result_times.append(result)

                if cost != results[i]:
                    temp = (cost - results[i]) / results[i]
                    errors = errors + temp

            error_level = (errors / repeats[i]) * 100.0
            saveFile = SaveToFile(output[j], file_names[i], file.vertices, results[i], paths[i], schemas[j], alpha,
                                  beta, rho, num_itr, q, error_level, result_times)
            saveFile.save()


if __name__ == "__main__":
    main()