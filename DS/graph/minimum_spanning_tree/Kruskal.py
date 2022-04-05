# Kruskal: O(E logE), edge 선택 기반 → edge의 개수가 적은 경우
# edge를 정렬한 후 union-find list를 이용하여 해당 edge가 서로 다른 tree를 연결하면 선택하여 E번 반복

import heapq


# graph = [[{distance} for _ in range(v)] for __ in range(v)] : 그래프의 정보를 저장한 인접행렬
# v = (# of vertices)
# e = (# of edges)

def kruskal():
    def find(x):
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]

    def union(x, y):
        uf[find(y)] = find(x)

    mst = []
    uf = list(range(v))
    edge_heap = []
    for s in range(v):
        for f in range(v):
            if graph[s][f] < INF:
                heapq.heappush(edge_heap, (graph[s][f], s, f))
    while edge_heap:
        w, s, f = heapq.heappop(edge_heap)
        if find(s) != find(f):
            mst.append([w, s, f])
            union(s, f)
    return mst
