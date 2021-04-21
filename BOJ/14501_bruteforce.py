# Problem : https://www.acmicpc.net/problem/14501
# Date : 2020-04-21

def solve(table, day, profit):
    if day > n:
        return sum(profit[:-1])
    elif day == n:
        return sum(profit)
    money = 0
    for i, task in enumerate(table[day:]):
        day += i+task[0]
        profit.append(task[1])
        money = max(money, solve(table, day, profit))
        day -= i+task[0]
        profit.pop()
    return money


n = int(input())
table = []
for _ in range(n):
    x = list(map(int, input().split()))
    table.append(x)

print(solve(table, 0, [0]))
