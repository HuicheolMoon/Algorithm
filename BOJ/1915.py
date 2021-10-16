# 가장 큰 정사각형
# Problem : https://www.acmicpc.net/problem/1915
# Date : 2021-10-16

import sys


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and arr[i][j] == 1:
            arr[i][j] += min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
        answer = max(answer, arr[i][j])
print(answer * answer)
