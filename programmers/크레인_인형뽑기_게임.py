# Problem : https://programmers.co.kr/learn/courses/30/lessons/64061
# Date : 2020-02-24

def solution(board, moves):
    answer = 0
    basket = []
    crane = 0
    for move in moves:
        # 1. 뽑기(board -> crane)
        for row in board:
            if row[move-1] != 0:
                crane = row[move-1]
                row[move-1] = 0
                break
        # 2. 넣기(crane -> basket)
        if crane != 0:
            basket.append(crane)
            crane = 0
        # 3. if 팡(in basket)
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket = basket[:-2]
            answer += 2
    return answer
