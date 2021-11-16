# 최단경로
# Problem : https://www.acmicpc.net/problem/1753
# Date : 2021-11-16

from collections import defaultdict
import heapq
import sys


graph = defaultdict(dict)
V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v not in graph[u]:
        graph[u][v] = w
        continue
    graph[u][v] = min(w, graph[u][v])
distances = {node: float("inf") for node in range(1, V+1)}
distances[k] = 0
queue = []
heapq.heappush(queue, [distances[k], k])
while queue:
    cur_dist, cur_loc = heapq.heappop(queue)
    if distances[cur_loc] >= cur_dist:
        for new_loc in graph[cur_loc]:
            dist = cur_dist + graph[cur_loc][new_loc]
            if dist < distances[new_loc]:
                distances[new_loc] = dist
                heapq.heappush(queue, [distances[new_loc], new_loc])
for i in range(1, V+1):
    print(distances[i] if distances[i] != float("inf") else "INF")
