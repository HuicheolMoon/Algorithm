# Problem : https://programmers.co.kr/learn/courses/30/lessons/86051
# Date : 2021-10-18
# 월간 코드 챌린지 시즌3: 없는 숫자 더하기
# 구현

def solution(numbers):
    answer = range_sum(0, 9) - sum(numbers)
    return answer


def range_sum(start, end):
    answer = (end + start) * (end - start + 1) // 2
    return answer
