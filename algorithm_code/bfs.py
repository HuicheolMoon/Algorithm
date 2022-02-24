# BFS


# v: # of vertices
# e: # of edges
# graph: 2D array for distances
# graph = [[distance for _ in range(v)] for __ in range(v)]]


# 1. Using queue
from collections import deque


def bfs(root):
    visited = [False for _ in range(v)]
    visited[root] = True
    queue = deque([root])
    while queue:
        start = queue.popleft()
        for i in range(v):
            if graph[start][i] > 0 and not visited[i]:
                visited[i] = True
                queue.append(i)
    return
