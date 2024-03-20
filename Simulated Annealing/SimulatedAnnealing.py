import math
import random


class SimulatedAnnealing:

    def __init__(self, graph, initial_temperature, cooling_rate, num_iterations):
        self.distance_matrix = graph.g
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations

    def acceptance_probability(self, current_distance, new_distance, temperature):
        if new_distance < current_distance or temperature == 0:
            return 1.0
        return math.exp((current_distance - new_distance) / temperature)

    def generate_initial_solution(self, num_cities):
        return random.sample(range(num_cities), num_cities)

    def generate_neighbor_solution_swap(self, current_solution):
        neighbor_solution = current_solution.copy()
        index1, index2 = random.sample(range(len(current_solution)), 2)
        neighbor_solution[index1], neighbor_solution[index2] = neighbor_solution[index2], neighbor_solution[index1]
        return neighbor_solution

    def rotate_fragment(self, solution):
        index1, index2, index3 = sorted(random.sample(range(len(solution)), 3))
        rotated_fragment = solution[index2:index3 + 1]
        rotated_fragment.reverse()
        new_solution = solution[:index2] + rotated_fragment + solution[index3 + 1:]
        return new_solution

    def generate_neighbor_solution_rotation(self, current_solution):
        neighbor_solution = self.rotate_fragment(current_solution)
        return neighbor_solution

    def calculate_total_distance(self, tour):
        total_distance = 0
        num_cities = len(tour)
        for i in range(num_cities - 1):
            total_distance += self.distance_matrix[tour[i]][tour[i + 1]]
        total_distance += self.distance_matrix[tour[-1]][tour[0]]  # Wrapping back to the starting city
        return total_distance

    # Geometric cooling
    def geometric_cooling(self, iteration):
        return self.initial_temperature * self.cooling_rate ** iteration

    # Logarithmic cooling
    def logarithmic_cooling(self, iteration):
        return self.initial_temperature / (1 + math.log(2 + iteration))

    def start(self, cooling_method, neighbor_method):
        num_cities = len(self.distance_matrix)
        current_solution = self.generate_initial_solution(num_cities)
        current_distance = self.calculate_total_distance(current_solution)
        best_solution = current_solution.copy()
        best_distance = current_distance

        temperature = self.initial_temperature

        for iteration in range(self.num_iterations):
            if neighbor_method == "swap":
                neighbor_solution = self.generate_neighbor_solution_swap(current_solution)
            if neighbor_method == "rotation":
                neighbor_solution = self.generate_neighbor_solution_rotation(current_solution)
            new_distance = self.calculate_total_distance(neighbor_solution)

            if self.acceptance_probability(current_distance, new_distance, temperature) > random.random():
                current_solution = neighbor_solution
                current_distance = new_distance

            if current_distance < best_distance:
                best_solution = current_solution.copy()
                best_distance = current_distance

            if cooling_method == "geo":
                temperature = self.geometric_cooling(iteration)
            if cooling_method == "log":
                temperature = self.logarithmic_cooling(iteration)

        return best_solution, best_distance
