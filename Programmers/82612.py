# Problem : https://programmers.co.kr/learn/courses/30/lessons/82612
# Date : 2021-10-19
# 위클리 챌린지: 1주차_부족한 금액 계산하기

def solution(price, money, count):
    less = price * (count * (count+1) // 2) - money
    if less > 0:
        answer = less
    else:
        answer = 0
    return answer
