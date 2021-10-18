# Problem : https://programmers.co.kr/learn/courses/30/lessons/17680
# Date : 2021-09-03
# 2018 KAKAO BLIND RECRUITMENT [1차] 캐시

import heapq


def solution(cacheSize, cities):
    answer = 0
    cache = []
    hit, miss = 1, 5
    if cacheSize == 0:
        answer = len(cities) * miss
        return answer
    for order, name in enumerate(cities):
        city = name.lower()
        for i in range(len(cache)):
            if cache[i][1] == city:
                answer += hit
                cache[i][0] = order
                heapq.heapify(cache)
                break
        else:
            answer += miss
            if len(cache) >= cacheSize:
                heapq.heappop(cache)
            heapq.heappush(cache, [order, city])
    return answer

