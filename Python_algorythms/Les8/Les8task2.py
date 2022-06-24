g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost


def dijkstra_pro(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    track = [[] for i in range(length)]
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    track[start].append(start)

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i in range(length):
        if not track[i]:
            ancestor = parent[i]
            while ancestor != -1:
                track[i].insert(0, ancestor)
                ancestor = parent[ancestor]
            track[i].append(i)
    return cost, track


n = int(input("Вершина: "))
cost, track = dijkstra_pro(g, n)

for i in range(len(g)):
    print(f'Стоимость пути {n} -> {i} равна {cost[i]}, маршрут: {" -> ".join(str(x) for x in track[i])}')



