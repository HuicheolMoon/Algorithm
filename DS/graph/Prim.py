# 간략한 prim algorithm 원리

import heapq


def prim(graph):
    mst = []
    vint = [0]
    edges = []
    while len(mst) < len(graph) - 1:
        for start in graph.keys():
            for dest, weight in graph[start]:
                if start in vint or dest in vint:
                    heapq.heappush(edges, (weight, start, dest))
        edge = heapq.heappop(edges)
        while edges:
            if edge[1] not in vint:
                vint.append(edge[1])
                mst.append(edge)
                break
            elif edge[0] not in vint:
                vint.append(edge[0])
                mst.append(edge)
                break
            edge = heapq.heappop(edges)
    return mst


a = {0: [(2, 5)], 1: [(0, 2)], 2: [(3, 3), (1, 1)], 3: [(0, 2), (1, 4)]}

print(prim(a))
