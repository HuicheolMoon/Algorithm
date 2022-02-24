# 탑
# Problem : https://www.acmicpc.net/problem/2493
# Date : 2022-02-24

n = int(input())
arr = list(map(int, input().split()))
answers = []
stack = []
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        stack.pop()
    if stack:
        answers.append(stack[-1] + 1)
    else:
        answers.append(0)
    stack.append(i)
print(" ".join(map(str, answers)))
