# 간략한 kruskal algorithm 원리

import heapq


def kruskal(graph):
    mst = []
    edges = []
    keys = list(graph.keys())
    uf = keys[:]
    for start in keys:
        for dest, weight in graph[start]:
            heapq.heappush(edges, (weight, start, dest))
    while len(mst) < len(graph) - 1:
        edge = heapq.heappop(edges)
        if uf[edge[1]] != uf[edge[2]]:
            mine, maxe = min(edge[1], edge[2]), max(edge[1], edge[2])
            uf[maxe] = uf[mine]
            mst.append(edge)
    return mst


a = {0: [(2, 5)], 1: [(0, 2)], 2: [(3, 3), (1, 1)], 3: [(0, 2), (1, 4)]}

print(kruskal(a))
