import priorityQueue


def astar(start_node, target_node, graph, x, y):
    open_set = priorityQueue.PriorityQueue()
    closed_set = []
    path = []
    current_node = None

    open_set.push(start_node)  # push start node into PQ

    while not open_set.is_empty():
        current_node = open_set.pop()  # take node with lowest f_cost
        if current_node == target_node:
            break

        closed_set.append(current_node)  # push this node to closed list as it's expanded
        neighbors = current_node.get_neighbors(graph, x, y)
