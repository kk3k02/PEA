import itertools


class Tsp:
    def __init__(self, n, cost):
        self.n = n  # Liczba punktów docelowych (miast)
        self.cost = cost  # Macierz kosztów odległości pomiędzy miastami

    # Metoda obliczająca całkowitą odległość trasy
    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(self.n - 1):
            start_node = path[i]
            end_node = path[i + 1]
            total_distance += self.cost[start_node][end_node]
        total_distance += self.cost[path[-1]][path[0]]  # Zamykanie trasy
        return total_distance

    # Metoda rozpoczynająca rozwiązywanie problemu
    def start(self):
        if self.n <= 2:
            return list(range(self.n)), 0  # Obsługa przypadków z mniej niż trzema punktami

        vertices = list(range(self.n))  # Lista punktów docelowych

        min_dist = float('inf')  # Początkowo zakładamy nieskończoną odległość
        best_path = None  # Początkowo brak najlepszej trasy

        # Przeszukiwanie wszystkich permutacji punktów docelowych
        for path in itertools.permutations(vertices):
            total_dist = self.calculate_total_distance(path)
            if total_dist < min_dist:
                min_dist = total_dist
                best_path = path

        best_path = list(best_path)
        best_path = best_path + [best_path[0]]  # Dodanie wierzchołka startowego na koniec trasy

        print("Path: ", best_path, " Cost: ", int(min_dist))

        return int(min_dist), best_path  # Zwracanie najlepszej trasy i kosztu drogi
