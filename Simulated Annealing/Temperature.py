import math
import random
from SimulatedAnnealing import SimulatedAnnealing


class Temperature:

    def __init__(self, graph):
        self.graph = graph.g
        self.num_ver = graph.vertices
        self.alpha = 1000000.0

    def find_initial_temperature(self):
        temperature = self.count_costs() / (self.num_ver * self.alpha)
        return temperature

    def count_costs(self):
        total_cost = 0
        n = len(self.graph)

        for i in range(n):
            for j in range(i + 1, n):
                total_cost += self.graph[i][j]

        return total_cost
