# 후위 표기식
# Problem : https://www.acmicpc.net/problem/1918
# Date : 2022-02-24

arr = list(input())
answer = []
stack = []
for char in arr:
    if char.isalpha():
        answer.append(char)
    elif char in ["+", "-"]:
        while stack and stack[-1] in ["*", "/", "+", "-"]:
            answer.append(stack.pop())
        stack.append(char)
    elif char in ["*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            answer.append(stack.pop())
        stack.append(char)
    elif char == "(":
        stack.append(char)
    elif char == ")":
        while stack and stack[-1] in ["*", "/", "+", "-"]:
            answer.append(stack.pop())
        if stack and stack[-1] == "(":
            stack.pop()
while stack:
    answer.append(stack.pop())
print("".join(answer))
