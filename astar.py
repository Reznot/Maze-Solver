import priorityQueue


def astar(start_node, target_node, graph, x, y):
    open_set = priorityQueue.PriorityQueue()
    closed_set = set()
    path = []
    current_node = None

    open_set.push(start_node)  # push start node into PQ

    while not open_set.is_empty():
        current_node = open_set.pop()  # take node with lowest f_cost
        if current_node == graph[target_node.x][target_node.y]:
            break

        closed_set.add(current_node)  # push this node to closed list as it's expanded
        neighbors = current_node.get_neighbors(graph, x, y)

        for neighbor in neighbors:
            if neighbor not in closed_set and not open_set.includes(neighbor): # Push node to open if is not in neither open or closed set
                neighbor.calc_f_cost(current_node, target_node)
                open_set.push(neighbor)

    while current_node.parent != current_node:
        path.insert(0, current_node)
        current_node = current_node.parent
    return path
