# Problem : https://programmers.co.kr/learn/courses/30/lessons/12979
# Date : 2021-10-23
# Summer/Winter Coding(~2018): 기지국 설치

def solution(n, stations, w):
    answer = 0
    left = 0
    scope = 2 * w + 1
    for station in stations:
        station -= 1
        right = station - w - 1
        if right >= left:
            interval = right - left
            answer += interval // scope + 1
        left = station + w + 1
    right = n - 1
    interval = right - left
    answer += interval // scope + 1
    return answer
