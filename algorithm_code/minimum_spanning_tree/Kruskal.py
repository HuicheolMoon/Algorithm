# Kruskal: O(E logE), edge 선택 기반 → edge의 개수가 적은 경우
# edge를 정렬한 후 union-find list를 이용하여 V-1번 반복

from collections import defaultdict
import heapq

graph = defaultdict(list) # graph[start] = list([end1, cost1], ...)


def kruskal(graph):
    mst = []
    edges = []
    keys = list(graph.keys())
    uf = keys[:] # union function
    for start in keys:
        for dest, weight in graph[start]:
            heapq.heappush(edges, (weight, start, dest))
    while len(mst) < len(graph) - 1:
        edge = heapq.heappop(edges)
        if uf[edge[1]] != uf[edge[2]]:
            mine, maxe = min(edge[1], edge[2]), max(edge[1], edge[2])
            for i in range(len(uf)):
                if uf[i] == maxe:
                    uf[i] = mine
            mst.append(edge)
    return mst
