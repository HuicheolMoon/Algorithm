# Problem : https://programmers.co.kr/learn/courses/30/lessons/12936
# Date : 2021-11-05
# 줄 서는 방법

def get_factorial(n):
    dp = [1 for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i
    return dp


def solution(n, k):
    answer = []
    factorial = get_factorial(n)
    candidates = list(range(1, n+1))
    while candidates:
        index, k = divmod((k-1) // factorial[len(candidates)-1])
        k += 1
        answer.append(candidates.pop(index))
    return answer
