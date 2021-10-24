# Problem : https://programmers.co.kr/learn/courses/30/lessons/12987
# Date : 2021-10-24
# Summer/Winter Coding(~2018): 숫자 게임

from bisect import bisect_right


def solution(A, B):
    answer = 0
    B.sort()
    for player_a in A:
        num_b = bisect_right(B, player_a)
        if num_b < len(B):
            answer += 1
            B.pop(num_b)
    return answer
