# BFS
edges = {"0" : [1, 2, 3, ...], ... }

def bfs(start):
    discovered = [False for _ in range(n)] # 정점 발견 여부
    queue = [] # 방문할 정점 목록
    order = [] # 정점 방문 순서
    queue.append(start)
    while queue:
        here = queue.pop(0)
        order.append(here)
        for there in edges[here]:
            if not discovered[there]:
                queue.append(there)
                discovered[there] = True
    return order

'''
1. 그래프 상 최단경로 -> distance 배열을 구현해서 discover마다 부모+1
'''

