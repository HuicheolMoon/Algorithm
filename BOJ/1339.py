# 단어 수학
# Problem : https://www.acmicpc.net/problem/1339
# Date : 2021-11-21

import sys


n = int(sys.stdin.readline())
counts = dict()
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    for i, char in enumerate(line):
        if char in counts:
            counts[char] += 10 ** (len(line) - i - 1)
        else:
            counts[char] = 10 ** (len(line) - i - 1)
nums = sorted(counts.values(), reverse=True)
answer = 0
pivot = 9
for num in nums:
    answer += num * pivot
    pivot -= 1
print(answer)
