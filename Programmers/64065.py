# Problem : https://programmers.co.kr/learn/courses/30/lessons/64065
# Date : 2021-09-03
# 2019 카카오 개발자 겨울 인턴십 - 튜플

def solution(s):
    answer = []
    parts = sorted([list(map(int, x.split(","))) for x in s[2:-2].split("},{")], key=lambda x: len(x))
    for i in range(len(parts)):
        if i == 0:
            answer.append(parts[i][0])
        else:
            answer.append(list(set(parts[i]) - set(parts[i-1]))[0])
    return answer
