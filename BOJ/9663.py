# N-Queen
# Problem : https://www.acmicpc.net/problem/9663
# Date : 2020-02-25

import sys


def n_queen(able, board):
    global n
    if len(board) == n:
        return 1
    cands = list(range(1, n+1))
    i = len(board)
    for h, hist in enumerate(board):
        arr = cands[:]
        for cand in arr:
            if not able[cand] or abs(cand - hist) == (i - h):
                cands.remove(cand)
    if len(cands) == 0:
        return 0
    answer = 0
    for cand in cands:
        board.append(cand)
        able[cand] = False
        answer += n_queen(able, board)
        board.remove(cand)
        able[cand] = True
    return answer


n = int(sys.stdin.readline().rstrip())
able = [True for _ in range(n+1)]
print(n_queen(able, []))
