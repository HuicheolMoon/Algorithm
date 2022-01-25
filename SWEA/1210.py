# [S/W 문제해결 기본] 2일차 - Ladder1
# Date : 2022-01-26


for _ in range(10):
    test_case = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    start_line = ladders.pop()
    point = start_line.index(2)
    ladders.reverse()
    for line in ladders:
        if point > 0 and line[point-1] == 1:
            while point > 0 and line[point-1] == 1:
                point -= 1
        elif point < 99 and line[point+1] == 1:
            while point < 99 and line[point+1] == 1:
                point += 1
    print(f"#{test_case} {point}")
