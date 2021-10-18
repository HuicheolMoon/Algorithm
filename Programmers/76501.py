# Problem : https://programmers.co.kr/learn/courses/30/lessons/76501
# Date : 2021-10-18
# 월간 코드 챌린지 시즌2: 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for ab, sn in zip(absolutes, signs):
        if sn:
            answer += ab
        else:
            answer -= ab
    return answer
