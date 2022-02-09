# Problem : https://programmers.co.kr/learn/courses/30/lessons/43236
# Date : 2022-02-09
# 징검다리

def solution(distance, rocks, n):
    rocks.sort()
    start = 0
    end = distance
    while start <= end:
        count = 0
        mid = (start + end) // 2
        pre = 0
        for rock in rocks:
            if rock - pre < mid:
                count += 1
                continue
            pre = rock
        if count > n:
            end = mid - 1
            continue
        start = mid + 1
    answer = end
    return answer
