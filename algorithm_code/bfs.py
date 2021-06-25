# BFS

from collections import defaultdict, deque

graph = defaultdict(list)
# graph[x].append(y) for edge in edges
# edge == [x: start, y: dest, (z: cost)]


def bfs(graph, root):
    # if dont know N(=len(nodes)), visited = [] & visited.append()
    visited = [[False, 0] for _ in range(N)]    # or [False, []]
    visited[root] = [True, 0]   # or [True, [root]]
    queue = deque([root])

# Obj function ----------

    while queue:
        start = queue.popleft()
        for dest in graph[start]:
            if not visited[dest][0]:
                visited[dest][0] = True
                queue.append(dest)
                visited[dest][1] = visited[start][1] + 1    # 새 정점을 방문하는 것이 항상 최단 경로
                # or visited[dest][1] = visited[start][1][:]
                # visited[dest][1].append(dest)

# Adjust Obj function value ----------

    return # target


'''
- 최단 경로 : obj : list일 때, [x[1] for x in visited]
- 최단 경로의 길이 : obj : int일 때, [x[1] for x in visited]
'''
