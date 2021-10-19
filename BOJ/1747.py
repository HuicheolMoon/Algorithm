# 소수&팰린드롬
# Problem : https://www.acmicpc.net/problem/1747
# Date : 2021-10-20

import sys
import math


def is_palindrome(num):
    arr = str(num)
    result = (arr == arr[::-1])
    return result


def is_prime(num):
    result = False
    if num == 1:
        return result
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return result
    result = True
    return result


n = int(sys.stdin.readline())
answer = n
while True:
    if is_palindrome(answer) and is_prime(answer):
        print(answer)
        break
    answer += 1
