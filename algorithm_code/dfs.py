# DFS

from collections import defaultdict

graph = defaultdict(list)
# graph[x].append(y) for edge in edges
# or graph = defaultdict(dict); graph[x][y] = z:cost


def dfs(graph, root):
    # if unknown N(=len(nodes)), visited = [] & visited.append()
    visited = [False for _ in range(N)]
    stack = [root] # stack = [[root, obj(root)]] for obj funcstion & value

# Obj function ----------

    while stack:
        start = stack.pop()
        if not visited[start]:
            visited[start] = True
            for dest in graph[start]:
                if not visited[dest]:
                    stack.append(dest)

# Adjust Obj function value ----------

    return #target


'''
- 두 정점 연결 여부 : 한 정점 root로 하고 dfs() 후 visited[other] (양방향 그래프의 단방향 연결 시 정점 스위칭)
- 독립 부분그래프 개수 : while (False in visited): root를 visited.index(False)로 반복한 횟수
- 방문 순서 : obj_list에 obj_list.append(start) 반복
'''
