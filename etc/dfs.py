# DFS - 모든 정점 발견
edges = {"0": [1, 2, 3, ...], ...}
visited = [False for _ in range(n)]

def dfs(here):
    visited[here] = True

    # 방문했을 때 변화하는 term에 대한 공간

    for there in edges[here]:
        if not visited[there]:
            dfs(there)

def main(edges, visited):
    for i in range(n): # 모든 간선이 다 연결되어 있지 않을 수 있기 때문에
        if not visited[i]:
            dfs(i)

'''
1. 그래프 상 두 정점의 연결 여부 -> dfs 1회 수행 후 visited 조사
2. 독립 부분그래프의 개수 -> main에서 dfs의 호출 횟수
3. 위상 정렬 -> dfs의 start 순서 저장해서 reverse
'''