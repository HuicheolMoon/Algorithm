# Problem : https://programmers.co.kr/learn/courses/30/lessons/92341
# Date : 2022-02-09
# 2022 KAKAO BLIND RECRUITMENT: 주차 요금 계산

from collections import defaultdict
import math


def solution(fees, records):
    park_times = defaultdict(int)
    for rec in records:
        time, car_num, action = rec.split()
        if action == "IN":
            park_times[car_num] += mod_time(time)
        elif action == "OUT":
            park_times[car_num] -= mod_time(time)
        else:
            pass
    park_costs = defaultdict(int)
    base_time, base_cost, unit_time, unit_cost = fees
    for car in park_times:
        time = park_times[car]
        cost = 0
        if time <= base_time:
            cost = base_cost
        else:
            cost = base_cost + math.ceil((time-base_time) / unit_time) * unit_cost
        park_costs[car] = cost
    answer = [y[1] for y in sorted(list(park_costs.items()), key=lambda x: x[0])]
    return answer


def mod_time(time):
    h, m = time.split(":")
    answer = (60 * 24 - 1) - (int(h) * 60 + int(m))
    return answer
