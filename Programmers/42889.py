# Problem : https://programmers.co.kr/learn/courses/30/lessons/42889
# Date : 2021-10-18
# 2019 KAKAO BLIND RECRUITMENT: 실패율

from collections import Counter, defaultdict


def solution(N, stages):
    fail_ratios = []
    not_clear = defaultdict(int, Counter(stages))
    arrival = len(stages)
    for i in range(1, N+1):
        f_ratio = 0
        if arrival > 0:
            f_ratio = not_clear[i] / arrival
        fail_ratios.append([i, f_ratio])
        arrival -= not_clear[i]
    answer = [y[0] for y in sorted(fail_ratios, key=lambda x: -x[1])]
    return answer
