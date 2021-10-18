# Problem : https://programmers.co.kr/learn/courses/30/lessons/67257
# Date : 2020-02-24
# 2020 카카오 인턴십 - 수식 극대화

from itertools import permutations


def solution(expression):
    answer = 0
    signs = ["+", "-", "*"]
    orders = list(map(list, permutations(signs)))
    for order in orders:
        answer = max(answer, abs(cal(expression, order)))
    return answer


def cal(expression: str, order: list) -> int:
    result = 1
    if not order:
        result = int(expression)
        return result
    sign = order.pop()
    nums = [cal(x, order) for x in expression.split(sign)]
    if len(nums) == 1:
        result = nums[0]
    elif sign == "+":
        result = sum(nums)
    elif sign == "-":
        result = nums[0] - sum(nums[1:])
    else:
        for num in nums:
            result *= num
    return result

