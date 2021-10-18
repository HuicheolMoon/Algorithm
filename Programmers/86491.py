# Problem : https://programmers.co.kr/learn/courses/30/lessons/86491
# Date : 2021-10-19
# 위클리 챌린지: 8주차_최소직사각형

def solution(sizes):
    wallet_long_side = 0
    wallet_short_side = 0
    for size in sizes:
        card_long_side = max(size)
        card_short_side = min(size)
        if card_long_side > wallet_long_side:
            wallet_long_side = card_long_side
        if card_short_side > wallet_short_side:
            wallet_short_side = card_short_side
        answer = wallet_long_side * wallet_short_side
    return answer
