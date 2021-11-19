# Prim: O(E logV), vertex 선택 기반 → edge의 개수가 많은 경우
# edge를 정렬한 후 한 vertex가 리스트에 있는 edge의 heap을 구성하고 최소 edge의 다른 vertex를 추가하여 V-1번 반복

from collections import defaultdict
import heapq

graph = defaultdict(list) # graph[start] = list([end1, cost1], ...)


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
            elif edge[2] not in vint:
                vint.append(edge[2])
                mst.append(edge)
                break
            edge = heapq.heappop(edges)
    return mst
