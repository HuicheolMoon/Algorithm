# 행렬 제곱
# Problem : https://www.acmicpc.net/problem/10830
# Date : 2021-10-29

from copy import deepcopy
import sys


def multiply_matrix(a, b):
    n = len(a)
    p = 1000
    result = deepcopy(a)
    e = [[1 if l == m else 0 for l in range(n)] for m in range(n)]
    if b == 1:
        b = e
    for i in range(n):
        for j in range(n):
            result[i][j] = sum([x * y for x, y in zip(a[i], [column[j] for column in b])]) % p
    return result


def solution(matrix, b):
    if b == 1:
        return multiply_matrix(matrix, 1)
    if b % 2 == 1:
        return multiply_matrix(solution(multiply_matrix(matrix, matrix), b // 2), matrix)
    return solution(multiply_matrix(matrix, matrix), b // 2)


n, b = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(n):
    low = [int(x) for x in sys.stdin.readline().split()]
    matrix.append(low)
answer = solution(matrix, b)
for low in answer:
    print(*low)
