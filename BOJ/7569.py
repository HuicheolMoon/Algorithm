# 토마토
# Problem : https://www.acmicpc.net/problem/7569
# Date : 2022-04-01

from collections import deque


def solution():
    global queue
    while queue:
        z, y, x = queue.popleft()
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                queue.append([nz, ny, nx])
    answer = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    return -1
            answer = max(max(arr[i][j])-1, answer)
    return answer


dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]
queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append([i, j, k])
print(solution())
