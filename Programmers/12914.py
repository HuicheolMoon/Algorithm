# Problem : https://programmers.co.kr/learn/courses/30/lessons/12914
# Date : 2021-10-05
# 멀리 뛰기

def solution(n):
    if n == 1:
        answer = 1
        return answer
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2
    pivot = 1234567
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        if dp[i] > pivot:
            dp[i] %= pivot
    answer = dp[n-1]
    return answer

