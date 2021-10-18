# Problem : https://programmers.co.kr/learn/courses/30/lessons/17682
# Date : 2021-10-19
# 2018 KAKAO BLIND RECRUITMENT: [1차] 다트 게임

def index_point(char):
    board = ["S", "D", "T"]
    return board.index(char) + 1


def solution(dart_result):
    board = []
    slide = False
    score = ""
    for char in dart_result:
        if char.isdigit():
            if slide:
                board.append(int(score))
                score = ""
            score += char
            slide = False
        elif char.isalpha():
            score = str(int(score) ** index_point(char))
            slide = True
        elif char == "*":
            if board:
                board[-1] *= 2
            score = str(int(score) * 2)
            slide = True
        else:
            score = str(-int(score))
    board.append(int(score))
    answer = sum(board)
    return answer
