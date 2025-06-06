def read_graph_from_csv(filename):
    with open(filename, 'r') as file:
        lines = [line.strip().split(',') for line in file if line.strip()]

    farms = lines[0]
    stores = lines[1]
    edges = lines[2:]

    graph = {}

    for u, v, cap in edges:
        cap = int(cap)
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = cap
        graph[v].setdefault(u, 0)

    graph['super_source'] = {}
    for farm in farms:
        graph['super_source'][farm] = float('inf')
        if farm not in graph:
            graph[farm] = {}
        graph[farm]['super_source'] = 0

    if 'super_sink' not in graph:
        graph['super_sink'] = {}
    for store in stores:
        if store not in graph:
            graph[store] = {}
        graph[store]['super_sink'] = float('inf')
        graph['super_sink'][store] = 0 

    return graph, 'super_source', 'super_sink'


def bfs(graph, source, sink, parent):
    visited = set()
    queue = [source]
    parent.clear()
    visited.add(source)

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                parent[v] = u
                if v == sink:
                    return True
                visited.add(v)
                queue.append(v)
    return False


def edmonds_karp(graph, source, sink):
    max_flow = 0
    parent = {}

    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


def main():
    graph, source, sink = read_graph_from_csv('road.csv')
    max_flow = edmonds_karp(graph, source, sink)
    print(f'Max number of cars that can deliver flowers per day: {int(max_flow)}')


if __name__ == '__main__':
    main()