# Bellman-Ford: 두 정점간의 최단거리 - O(EV)
# 모든 edge에 대해서 도착점을 제외한 v-1개의 정점에 대해 최단경로 갱신을 반복
# Dijkstra와 다른 점: 모든 경우에 대해 최단경로를 갱신하기 때문에 일반적으로 dijkstra보다 느리지만 음의 가중치가 있는 경우에도 최단경로 계산 가능


# graph = [[{distance} for _ in range(v)] for __ in range(v)] : 그래프의 정보를 저장한 인접행렬
# v = (# of vertices)
# e = (# of edges)

def bellman_ford(graph, root):
    distance_list = [float("inf") for _ in range(v)]  # root로부터의 거리
    distance_list[root] = 0
    # 알고리즘 작동 단계
    for _ in range(v-1):    # V
        for s in range(v):  # E (모든 vertices pair 중 edge가 연결된 pair만 선택하여 연산하므로)
            for f in range(v):
                if graph[s][f] < INF:
                    new_distance = distance_list[s] + graph[s][f]
                    if new_distance < distance_list[f]:
                        distance_list[f] = new_distance
    # 음수 사이클 검증 단계
    for s in range(v):
        for f in range(v):
            new_distance = distance_list[s] + graph[s][f]
            if new_distance < distance_list[f]:
                # 모든 정점에 대해 최단경로를 갱신해도 다른 최단경로가 존재 == 음수 사이클이 존재 -> 최단거리가 존재하지 않음
                return "Failure"
    return distance_list
