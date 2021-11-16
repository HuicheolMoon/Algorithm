# 평범한 배낭
# Problem : https://www.acmicpc.net/problem/12865
# Date : 2021-11-16

n, k = list(map(int, input().split()))
specs = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k+1)]
for i in range(n):
    for j in range(k, 0, -1):
        if specs[i][0] <= j:
            dp[j] = max(dp[j], dp[j-specs[i][0]] + specs[i][1])
print(dp[k])
