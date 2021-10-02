# Problem : https://programmers.co.kr/learn/courses/30/lessons/42898
# Date : 2021-10-03
# 등굣길

def solution(m, n, puddles):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for y in range(n):
        for x in range(m):
            if [x+1, y+1] in puddles:
                dp[x][y] = 0
            elif x == 0:
                dp[x][y] = dp[x][y-1]
            elif y == 0:
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = (dp[x-1][y] + dp[x][y-1]) % 1000000007
    return dp[-1][-1]
