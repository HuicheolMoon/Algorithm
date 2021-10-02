# Problem : https://programmers.co.kr/learn/courses/30/lessons/43105
# Date : 2021-10-03
# 정수 삼각형

def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(i+1)] for i in range(n)]
    for j in range(n):
        if j == 0:
            dp[0][0] = triangle[0][0]
            continue
        for k in range(j+1):
            if k == 0 or k == j:
                dp[j][k] = dp[j-1][-k//j] + triangle[j][k]
            else:
                dp[j][k] = max(dp[j-1][k-1], dp[j-1][k]) + triangle[j][k]
    answer = max(dp[-1])
    return answer
