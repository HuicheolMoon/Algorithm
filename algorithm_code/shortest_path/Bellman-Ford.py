# Bellman-Ford: 두 정점간의 최단거리 - O(EV)

from collections import defaultdict

# graph = defaultdict(dict) -> graph[x][y] = cost


def bellman_ford(graph, root):
    distances = {node: float("inf") for node in graph}  # root로부터의 거리
    distances[root] = 0

    for _ in range(len(graph) - 1):
        for start, x in graph.items():
            for dest, cost in x.items():
                dist = distances[start] + cost
                if distances[dest] > dist:
                    distances[dest] = dist

    for node in graph:
        for neighbor, cost in graph[node].items():
            dist = distances[node] + cost
            if distances[neighbor] > dist:
                return "Failure"

    return distances
