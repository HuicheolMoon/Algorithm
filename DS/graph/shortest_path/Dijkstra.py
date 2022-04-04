# Dijkstra: 두 정점간의 최단거리 - 음의 가중치가 없을 때. O(E logV), heap
# root에서부터 Greedy하게 가장 가까운 정점의 최단거리를 갱신/반복


import heapq


# graph = [[{distance} for _ in range(v)] for __ in range(v)] : 그래프의 정보를 저장한 인접행렬
# v = (# of vertices)
# e = (# of edges)

def dijkstra(graph, root):
    distance_list = [float("inf") for _ in range(v)]  # root로부터의 거리
    distance_list[root] = 0
    queue = []
    heapq.heappush(queue, [distance_list[root], root])
    while queue:
        distance, s = heapq.heappop(queue)
        if distance_list[s] >= distance:
            # 갱신 가능성이 있는 정점인 경우
            for f in range(v):
                if graph[s][f] < INF:
                    new_distance = distance + graph[s][f]
                    if new_distance < distance_list[f]:
                        distance_list[f] = new_distance
                        heapq.heappush(queue, [distance_list[f], f])
    return distance_list
