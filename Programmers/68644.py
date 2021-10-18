# Problem : https://programmers.co.kr/learn/courses/30/lessons/68644
# Date : 2021-10-19
# 월간 코드 챌린지 시즌1: 두 개 뽑아서 더하기

from itertools import combinations


def solution(numbers):
    return sorted(list(set(x + y for x, y in list(combinations(numbers, 2)))))
