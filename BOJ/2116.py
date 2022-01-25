# 주사위 쌓기
# Problem : https://www.acmicpc.net/problem/2116
# Date : 2022-01-26

import sys


n = int(sys.stdin.readline())
relations = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
dices = []
for _ in range(n):
    dice = list(map(int, sys.stdin.readline().split()))
    dices.append(dice)
max_total = 0
for i in range(1, 7):
    total = 0
    base = i
    for dice in dices:
        candidates = dice[:]
        opposite = dice[relations[dice.index(base)]]
        candidates.remove(base)
        candidates.remove(opposite)
        total += max(candidates)
        base = opposite
    max_total = max(max_total, total)
print(max_total)
