# Problem : https://www.acmicpc.net/problem/14888
# Date : 2020-04-21

def cal(x, y, mode):
    if mode == 0:
        return x+y
    if mode == 1:
        return x-y
    if mode == 2:
        return x*y
    if mode == 3:
        return x//y if x > 0 else -(abs(x)//y)

def solve(arr, symbol, num):
    global answers
    if len(arr) == 0:
        answers.append(num)
        return 0
    for i in range(4):
        if i == 4 and arr[0] == 0:
            return 0
        if symbol[i] > 0:
            new_num = cal(num, arr[0], i)
            symbol[i] -= 1
            solve(arr[1:], symbol, new_num)
            symbol[i] += 1
    return 0


answers = []
n = int(input())
arr = list(map(int, input().split()))
symbol = list(map(int, input().split()))
p = arr.pop(0)
solve(arr, symbol, p)
print(max(answers))
print(min(answers))
