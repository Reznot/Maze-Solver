import math


class Node:
    def __init__(self, x, y, color):
        self.reachable = color[0] != 0
        self.x = x
        self.y = y
        self.parent = None

        # cost function for Astar; Initially are infinite
        self.g_cost = math.inf
        self.h_cost = math.inf
        self.f_cost = math.inf

    def euclidean_distance(self, target):
        return math.sqrt((target.x - self.x) ** 2 + (target.y - self.y) ** 2)
