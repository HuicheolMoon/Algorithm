# Problem : https://programmers.co.kr/learn/courses/30/lessons/92344
# Date : 2022-04-13
# 2022 KAKAO BLIND RECRUITMENT: 파괴되지 않은 건물

def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for skill_type, r1, c1, r2, c2, degree in skill:
        power = degree * int((skill_type - 1.5) * 2)
        dp[r1][c1] += power
        dp[r1][c2+1] -= power
        dp[r2+1][c1] -= power
        dp[r2+1][c2+1] += power
    for i in range(n+1):
        for j in range(1, m+1):
            dp[i][j] += dp[i][j-1]
    for i in range(m+1):
        for j in range(1, n+1):
            dp[j][i] += dp[j-1][i]
    for i in range(n):
        for j in range(m):
            if board[i][j] + dp[i][j] > 0:
                answer += 1
    return answer
