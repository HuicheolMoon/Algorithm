# Problem : https://programmers.co.kr/learn/courses/30/lessons/70129
# Date : 2021-10-19
# 월간 코드 챌린지 시즌1: 이진 변환 반복하기

import re


def solution(s):
    num = 0
    count = 0
    while s != "1":
        num += s.count("0")
        s = re.sub("0", "", s)
        s = bin(len(s))[2:]
        count += 1
    answer = [count, num]
    return answer
