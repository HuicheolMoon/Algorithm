# Problem : https://programmers.co.kr/learn/courses/30/lessons/17687
# Date : 2021-09-03
# 2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임

from collections import deque


def solution(n, t, m, p):
    answer = ''
    queue = deque([])
    num = 0
    order = 0
    while t > 0:
        if not queue:
            queue = deque(list(base_n(num, n)))
            num += 1
        char = queue.popleft()
        if order % m == (p - 1):
            answer += char
            t -= 1
        order += 1
    return answer


def base_n(num, n):
    result = ""
    alpha = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    if num == 0:
        return "0"
    while num > 0:
        char = num % n
        if char >= 10:
            char = alpha[char]
        else:
            char = str(char)
        result = char + result
        num //= n
    return result
