# Dijkstra: 두 정점간의 최단거리 - 음의 가중치가 없을 때. O(E logV), heap

from collections import defaultdict
import heapq

# graph = defaultdict(dict) -> graph[x][y] = cost


def dijkstra(graph, root):
    distances = {node: float("inf") for node in graph}  # root로부터의 거리
    distances[root] = 0
    queue = []
    heapq.heappush(queue, [distances[root], root])

    while queue:
        cur_dist, cur_loc = heapq.heappop(queue)
        if distances[cur_loc] >= cur_dist:
            for new_loc, new_dist in graph[cur_loc].items():
                dist = cur_dist + new_dist
                if dist < distances[new_loc]:
                    distances[new_loc] = dist
                    heapq.heappush(queue, [distances[new_loc], new_loc])

    return distances
