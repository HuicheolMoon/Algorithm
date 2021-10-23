# Problem : https://programmers.co.kr/learn/courses/30/lessons/42884
# Date : 2021-10-23
# 단속 카메라

def solution(routes):
    routes.sort(key=lambda x: -x[1])
    answer = 0
    while routes:
        target_car = routes.pop()
        camera = target_car[1]
        answer += 1
        candidates = routes[:]
        for car in routes:
            if car[0] <= camera <= car[1]:
                candidates.remove(car)
        routes = candidates
    return answer
