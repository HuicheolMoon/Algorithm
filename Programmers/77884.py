# Problem : https://programmers.co.kr/learn/courses/30/lessons/77884
# Date : 2021-10-18
# 월간 코드 챌린지 시즌2: 약수의 개수와 덧셈

import math


def solution(left, right):
    answer = 0
    nums = list(range(left, right + 1))
    for n in nums:
        if n_div_is_even(n):
            answer += n
        else:
            answer -= n
    return answer


def n_div_is_even(n):
    return n != int(math.sqrt(n)) ** 2
