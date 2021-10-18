# Problem : https://programmers.co.kr/learn/courses/30/lessons/68935
# Date : 2021-10-18
# 월간 코드 챌린지 시즌1: 3진법 뒤집기

def solution(n):
    p = 3
    return int(base_p(n, p)[::-1], p)


def base_p(n: int, p: int) -> str:
    if p < 2:
        raise ValueError("The base is impossible value.")
    answer = ""
    while n > 0:
        answer = str(n % p) + answer
        n //= p
    return answer
