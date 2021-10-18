# Problem : https://programmers.co.kr/learn/courses/30/lessons/62048
# Date : 2021-10-18
# Summer/Winter Coding(2019): 멀쩡한 사각형

import math


def solution(w,h):
    gcd = math.gcd(w, h)
    long, short = max(w, h) / gcd, min(w, h) / gcd
    space = long + (short - 1)
    space *= gcd
    answer = (w * h) - space
    return answer
