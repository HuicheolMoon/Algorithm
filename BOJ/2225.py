# 합분해
# Problem : https://www.acmicpc.net/problem/2225
# Date : 2021-10-29

import sys


n, k = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(k+1)] for __ in range(n+1)]
# dp[n][k] = 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
pivot = 1000000000
for a in range(n+1):
    dp[a][1] = 1
for b in range(1, k+1):
    dp[0][b] = 1
for i in range(2, k+1):
    for j in range(1, n+1):
        dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % pivot
print(dp[n][k])
