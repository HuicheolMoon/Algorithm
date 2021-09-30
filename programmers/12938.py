# Problem : https://programmers.co.kr/learn/courses/30/lessons/12938
# Date : 2020-10-01
# 연습문제 최고의 집합

def solution(n, s):
    answer = []
    if n > s:
        answer = [-1]
        return answer
    base = s // n
    delta = s % n
    answer = [base] * (n - delta) + [base + 1] * delta
    return answer
