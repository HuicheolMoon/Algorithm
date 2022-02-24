# 알파벳
# Problem : https://www.acmicpc.net/problem/1987
# Date : 2022-02-24

import sys


def solution(start):
    max_length = 1
    queue = {start}
    while queue:
        if max_length >= 26:
            return max_length
        y, x, route = queue.pop()
        for m in range(4):
            ny = y + dy[m]
            nx = x + dx[m]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if arr[ny][nx] not in route:
                queue.add((ny, nx, route+arr[ny][nx]))
                max_length = max(len(route)+1, max_length)
    return max_length


r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
print(solution((0, 0, arr[0][0])))
