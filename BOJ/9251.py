# LCS
# Problem : https://www.acmicpc.net/problem/9251
# Date : 2021-11-16

import sys


a = " " + sys.stdin.readline().rstrip()
b = " " + sys.stdin.readline().rstrip()
arr = [[0 for _ in range(len(a))] for __ in range(len(b))]
for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[j] == b[i]:
            arr[i][j] = arr[i-1][j-1] + 1
            continue
        arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[-1][-1])
