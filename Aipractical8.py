import heapq

def astar_search(graph, heuristics, start, goal):

    open_list = [(heuristics[start], 0, start, [start])]
    closed_set = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

     
        if node == goal:
            return path, g

        closed_set.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor in closed_set:
                continue

            g_new = g + cost
            f_new = g_new + heuristics[neighbor]

            skip = False
            for item in open_list:
                if item[2] == neighbor and item[1] <= g_new:
                    skip = True
                    break
            if skip:
                continue

            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')


graph = {
      'S': {'A': 1, 'B': 4},
   	'A': {'B': 2, 'C': 5, 'D': 12},
	'B': {'C': 2},
	'C': {'D': 3, 'G': 7},
	'D': {'G': 2},
	'G': {}
}

heuristics = {
	'S': 7, 'A': 6, 'B': 4,
	'C': 2, 'D': 1, 'G': 0
}


start, goal = 'S', 'G'
path, cost = astar_search(graph, heuristics, start, goal)

if path:
    print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
    print(f"Total (optimal) cost: {cost}")
else:
    print("No path found.")


