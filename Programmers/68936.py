# Problem : https://programmers.co.kr/learn/courses/30/lessons/68936
# Date : 2021-11-10
# 월간 코드 챌린지 시즌1: 쿼드압축 후 개수 세기

def solution(arr):
    answer = [0, 0]
    if is_unique(arr):
        answer[arr[0][0]] = 1
        return answer
    answer = [sum(x) for x in zip(answer, *[solution(subarr) for subarr in quad_division(arr)])]
    return answer


def is_unique(arr):
    unique = True
    n = len(arr)
    pivot = 1 - arr[0][0]
    if n == 1:
        return unique
    for row in arr:
        if pivot in row:
            unique = False
            return unique
    return unique


def quad_division(arr):
    n = len(arr)
    subarrs = []
    for x in range(2):
        for y in range(2):
            subarr = [row[(n//2)*y:n//(2-y)] for row in arr[(n//2)*x:n//(2-x)]]
            subarrs.append(subarr)
    return subarrs
