# Floyd-Warchall: 모든 vertex 쌍에 대한 최단거리 - O(V^3)
# 완전탐색: 모든 가능한 부분경로에 대해서 최단경로 갱신
# 모든 정점 쌍에 대하여 최단거리 계산 (return이 2D array)


# graph = [[{distance} for _ in range(v)] for __ in range(v)] : 그래프의 정보를 저장한 인접행렬
# v = (# of vertices)
# e = (# of edges)

def floyd_warshall(graph):
    distance_list = [[float("inf") for _ in range(v)] for __ in range(v)]
    for s in range(v):
        for f in range(v):
            if graph[s][f] < INF:
                distance_list[s][f] = graph[s][f]
    # 모든 중간 정점에 대해 모든 시작점과 끝 점 사이의 최단경로를 갱신 (중간 정점 선택 우선)
    for m in range(v):
        for s in range(v):
            for f in range(v):
                new_distance = distance_list[s][m] + distance_list[m][f]
                if new_distance < distance_list[s][f]:
                    distance_list[s][f] = new_distance
    return distance_list
