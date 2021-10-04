# 검문
# Problem : https://www.acmicpc.net/problem/2981
# Date : 2020-02-25

from sys import stdin
import math

n = int(stdin.readline())
nums = []
answer = []
for _ in range(n):
    nums.append(int(stdin.readline()))
pivot = min(nums)
arr = [x-pivot for x in nums if x-pivot != 0]
gcd = math.gcd(*arr)
for i in range(2, int(math.sqrt(gcd))+1):
    if gcd % i == 0:
        answer.append(i)
for x in answer[::-1]:
    if x != gcd // x:
        answer.append(gcd//x)
answer.append(gcd)
print(" ".join(map(str, answer)))
