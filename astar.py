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
            print('elo')
            break

        closed_set.add(current_node)  # push this node to closed list as it's expanded
        print(f'closed: {len(closed_set)}')
        neighbors = current_node.get_neighbors(graph, x, y)

        for neighbor in neighbors:
            if neighbor not in closed_set:
                is_better = neighbor.check_if_better(current_node, target_node)
                if is_better and not open_set.includes(neighbor):
                    open_set.push(neighbor)
        print(f'open: {open_set.len()}')

    while current_node.parent != current_node:
        path.insert(0, current_node)
        current_node = current_node.parent
    return path
