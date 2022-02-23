# DFS


# v: # of vertices
# e: # of edges
# graph: 2D array for distances
# graph = [[distance for _ in range(v)] for __ in range(v)]]


# 1. Using stack
def dfs(root):
    stack = [root]
    visited = [False for _ in range(v)]
    while stack:
        start = stack[-1]
        for i in range(v):
            if graph[start][i] > 0 and not visited[i]:
                visited[i] = True
                stack.append(i)
                break
        else:
            stack.pop()
    return


# 2. Recursion
visited = [False for _ in range(v)]


def dfs(start):
    visited[start] = True
    for i in range(v):
        if graph[start][i] > 0 and not visited[i]:
            dfs(i)
    return
