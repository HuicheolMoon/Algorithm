# BFS: deque(양방향 큐)

# graph = [[{distance} for _ in range(v)] for __ in range(v)]]; 그래프의 정보를 저장한 인접행렬
# v = (# of vertices)
# e = (# of edges)

from collections import deque


def bfs(root):
    visited = [False for _ in range(v)]
    visited[root] = True
    queue = deque([root])
    while queue:
        s = queue.popleft()
        for f in range(v):
            if graph[s][f] < INF and not visited[f]:
                visited[f] = True
                queue.append(f)
