# Problem : https://programmers.co.kr/learn/courses/30/lessons/12977
# Date : 2021-10-18
# Summer/Winter Coding(~2018): 소수 만들기

import math
from itertools import combinations


def solution(nums):
    answer = 0
    for x in combinations(nums, 3):
        if is_prime(sum(x)):
            answer += 1
    return answer


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
