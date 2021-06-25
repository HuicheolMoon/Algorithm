# Floyd-Warchall: 모든 vertex 쌍에 대한 최단거리 - O(V^3)

from collections import defaultdict

# graph = defaultdict(dict) -> graph[x][y] = cost


def floyd_warshall(graph):
    N = len(graph)
    distances = [[float("inf")] * N for _ in range(N)]  # assume that keys() == range()

    for start, x in graph.items():
        for dest, cost in x.items():
            distances[start][dest] = cost

    for mid in range(N):
        for start in range(N):
            for dest in range(N):
                new_dist = distances[start][mid] + distances[mid][dest]
                if distances[start][dest] > new_dist:
                    distances[start][dest] = new_dist

    return distances
