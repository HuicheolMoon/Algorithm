# 두 용액
# Problem : https://www.acmicpc.net/problem/2470
# Date : 2021-10-04

import sys


def solution(n, arr):
    ph_arr = sorted(arr)
    answer = []
    left = 0
    right = len(ph_arr) - 1
    min_mix_property_abs = 10 ** 9
    if ph_arr[0] >= -1:
        answer = ph_arr[:2]
        return answer
    if ph_arr[-1] <= 1:
        answer = ph_arr[-2:]
        return answer
    while left < right:
        pair = [ph_arr[left], ph_arr[right]]
        mix_property = sum(pair)
        if abs(mix_property) < min_mix_property_abs:
            answer = pair[:]
            min_mix_property_abs = abs(mix_property)
        if mix_property == 0:
            return answer
        elif mix_property > 0:
            right -= 1
        else:
            left += 1
    return answer


n = int(sys.stdin.readline())  # int
arr = list(map(int, sys.stdin.readline().split()))  # List[int]
print(*solution(n, arr))
