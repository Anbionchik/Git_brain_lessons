graph = {
    0: {1, 3},
    1: {3, 5},
    2: {3},
    3: {},
    4: {2},
    5: {4}
}


def create_graph(n):
    return {x:{z for z in range(n) if z != x} for x in range(n)}


def traversing_graph(graph, start):
    length = len(graph)
    is_visited = [False] * length

    def dfs(node):
        print(f'{node} -> ', end='')
        is_visited[node] = True
        for i in graph[node]:
            if not is_visited[i]:
                dfs(i)

    dfs(start)


traversing_graph(graph, 0)
print()
graph_auto = create_graph(10)
traversing_graph(graph_auto, 5)



