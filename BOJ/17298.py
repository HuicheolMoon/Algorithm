# 오큰수
# Problem : https://www.acmicpc.net/problem/17298
# Date : 2020-02-25

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1 for _ in range(n)]

for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        comp = stack.pop()
        answer[comp] = arr[i]
    stack.append(i)
print(" ".join(map(str, answer)))
