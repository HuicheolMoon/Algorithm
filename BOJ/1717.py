# 집합의 표현
# Problem : https://www.acmicpc.net/problem/1717
# Date : 2021-11-16

import sys


def get_root(n):
    if n == parents[n]:
        return n
    paths = []
    root = n
    while root != parents[root]:
        paths.append(parents[root])
        root = parents[root]
    for path in paths:
        parents[path] = root
    return root


n, m = map(int, sys.stdin.readline().split())
parents = list(range(n+1))
for _ in range(m):
    operator, a, b = map(int, sys.stdin.readline().split())
    root_a = get_root(a)
    root_b = get_root(b)
    if operator == 1:
        print("YES" if root_a == root_b else "NO")
    elif root_a > root_b:
        parents[root_a] = root_b
    elif root_a <= root_b:
        parents[root_b] = root_a
