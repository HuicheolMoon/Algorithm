# Problem : https://programmers.co.kr/learn/courses/30/lessons/17679
# Date : 2021-09-03
# 2018 KAKAO BLIND RECRUITMENT [1차] 프렌즈4블록

def solution(m, n, board):
    answer = 0
    game_board = [] # board를 clockwise 90도 회전 (가로 m * 세로 n) : [block, is_bang]
    for x in range(n):
        low = []
        for y in range(m-1, -1, -1):
            low.append([board[y][x], False])
        game_board.append(low)
    bang = True
    while bang:
        bang = False
        for y in range(1, n):
            for x in range(1, m):
                cands = [game_board[h][w][0] for h, w in [(y, x), (y, x-1), (y-1, x), (y-1, x-1)]]
                if (len(set(cands)) == 1) and (cands[0] != "."):
                    for h, w in [(y, x), (y, x-1), (y-1, x), (y-1, x-1)]:
                        game_board[h][w][1] = True
                    bang = True
        for y in range(n):
            new_low = [block for block in game_board[y] if not block[1]]
            blank = m - len(new_low)
            answer += blank
            new_low.extend([[".", False]] * blank)
            game_board[y] = new_low
    return answer

