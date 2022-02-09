# Problem : https://programmers.co.kr/learn/courses/30/lessons/92335
# Date : 2022-02-09
# 2022 KAKAO BLIND RECRUITMENT: k진수에서 소수 개수 구하기

import math


def solution(n, k):
    origin = convert_base(n, k)
    cands_prime = [x for x in origin.split("0") if x != "" and is_prime(int(x))]
    answer = len(cands_prime)
    return answer


def convert_base(n, k):
    q, r = divmod(n, k)
    if q == 0:
        return str(n)
    return convert_base(q, k) + str(r)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
