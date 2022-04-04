# DFS: recursion or stack

# graph = [[{distance} for _ in range(v)] for __ in range(v)]]; 그래프의 정보를 저장한 인접행렬
# v = (# of vertices)
# e = (# of edges)


# 1. Recursion
visited = [False for _ in range(v)]


def dfs(s):
    global visited
    for f in range(v):
        if graph[s][f] < INF and not visited[f]:
            visited[f] = True
            dfs(f)
            visited[f] = False


# 2. Using stack
def dfs(root):
    visited = [False for _ in range(v)]
    stack = [root]
    while stack:
        s = stack[-1]
        for f in range(v):
            if graph[s][f] < INF and not visited[f]:
                visited[f] = True
                stack.append(f)
                break
        else:
            stack.pop()
