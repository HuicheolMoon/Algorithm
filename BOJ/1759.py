# 암호 만들기
# Problem : https://www.acmicpc.net/problem/1759
# Date : 2021-10-20

import sys
from itertools import combinations


l, c = map(int, sys.stdin.readline().split())
candidates = sys.stdin.readline().split()
candidates.sort()

vowels = set(["a", "e", "i", "o", "u"])

for case in combinations(candidates, l):
    word = set(case)
    if 1 <= len(word.intersection(vowels)) <= l - 2:
        password = "".join(case)
        print(password)
