import math


class Node:
    def __init__(self, x, y, color):
        self.reachable = color != 0
        self.x = x
        self.y = y
        self.parent = None

        # cost function for Astar; Initially are infinite
        self.g_cost = math.inf
        self.h_cost = math.inf
        self.f_cost = math.inf

    def euclidean_distance(self, target):
        return math.sqrt((target.x - self.x) ** 2 + (target.y - self.y) ** 2)

    def set_start_node(self, target):
        self.g_cost = 0
        self.h_cost = self.euclidean_distance(target)
        self.f_cost = self.g_cost + self.h_cost
        self.parent = self

    def get_neighbors(current_node, graph, x, y):
        neighbors = []
        if current_node.x > 0:
            if graph[current_node.x - 1][current_node.y].reachable:
                neighbors.append(graph[current_node.x - 1][current_node.y])

        return neighbors
