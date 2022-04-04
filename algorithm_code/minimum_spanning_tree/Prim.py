# Prim: O(E logV), vertex 선택 기반 → edge의 개수가 많은 경우
# 한 vertex가 tree에 속한 edge의 heap을 구성하고 최소 weight인 edge의 다른 vertex를 tree에 추가하여 V-1번 반복

import heapq


# graph = [[{distance} for _ in range(v)] for __ in range(v)] : 그래프의 정보를 저장한 인접행렬

def prim():
    v, e = map(int, input().split())    # v: # of vertices / e: # of edges
    visited = [False for _ in range(v+1)]   # 각 node가 mst에 포함되는지 체크하는 배열
    root = 0    # 임의의 초기 node 설정
    visited[root] = True
    mst = []
    edge_heap = []
    for node in range(v):
        heapq.heappush(edge_heap, [graph[root][node], root, node])
    while len(mst) < v - 1: # mst의 길이는 (# of vertice) - 1
        w, s, m = heapq.heappop(edge_heap)
        if not visited[m]:
            visited[m] = True
            mst.append([w, s, m])
            for f in range(v):
                if graph[m][f] < float('inf') and not visited[f]:
                    heapq.heappush(edge_heap, [graph[m][f], m, f])
    return mst
