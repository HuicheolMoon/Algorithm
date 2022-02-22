# 문자열 폭발
# Problem : https://www.acmicpc.net/problem/9935
# Date : 2022-02-22

arr = list(input())
bomb = list(input())
stack = []
for char in arr:
    stack.append(char)
    if char == bomb[-1] and len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]
if stack:
    print("".join(stack))
else:
    print("FRULA")
