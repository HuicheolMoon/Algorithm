# Problem : https://programmers.co.kr/learn/courses/30/lessons/12900
# Date : 2021-10-03
# 2 x n 타일링

def solution(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    answer = dp[n-1]
    return answer

