# Problem : https://programmers.co.kr/learn/courses/30/lessons/12978
# Date : 2021-10-23
# Summer/Winter Coding(~2018): 배달

import heapq


def dijkstra(graph, root):
    n = len(graph)
    distances = [float("inf") for _ in range(n)]
    distances[root] = 0
    queue = []
    heapq.heappush(queue, [distances[root], root])
    while queue:
        cur_dist, cur_loc = heapq.heappop(queue)
        if distances[cur_loc] >= cur_dist:
            for new_loc, new_dist in enumerate(graph[cur_loc]):
                dist = cur_dist + new_dist
                if dist < distances[new_loc]:
                    distances[new_loc] = dist
                    heapq.heappush(queue, [distances[new_loc], new_loc])
    return distances


def solution(N, road, K):
    graph = [[float("inf") for _ in range(N)] for __ in range(N)]
    for way in road:
        a, b, c = way[0] - 1, way[1] - 1, way[2]
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    root = 0
    distances = dijkstra(graph, root)
    answer = 0
    for town_dist in distances:
        if town_dist <= K:
            answer += 1
    return answer
