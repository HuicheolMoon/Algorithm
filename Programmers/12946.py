# Problem : https://programmers.co.kr/learn/courses/30/lessons/12946
# Date : 2021-10-03
# 하노이의 탑

def solution(n):
    dp = [[]] * n
    dp[0] = [[1, 3]]
    for i in range(1, n):
        dp[i] = trans(dp[i-1], "front") + dp[0] + trans(dp[i-1], "back")
    answer = dp[n-1]
    return answer


def trans(arr, mode):
    trans_dict = dict()
    if mode == "front":
        trans_dict = {1: 1, 2: 3, 3: 2}
    elif mode == "back":
        trans_dict = {1: 2, 2: 1, 3: 3}
    else:
        raise Exception("mode error")
    result = [[trans_dict[y] for y in x] for x in arr]
    return result

