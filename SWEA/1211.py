# [S/W 문제해결 기본] 2일차 - Ladder2
# Date : 2022-01-26


for _ in range(10):
    test_case = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    start_line = ladders[0]
    points = [i for i in range(100) if start_line[i] == 1]
    answer = points[0]
    min_distance = 100 * 100
    for point in points:
        start = point
        distance = 100
        for line in ladders:
            if point > 0 and line[point-1] == 1:
                while point > 0 and line[point-1] == 1:
                    point -= 1
                    distance += 1
            elif point < 99 and line[point+1] == 1:
                while point < 99 and line[point+1] == 1:
                    point += 1
                    distance += 1
        if distance <= min_distance:
            answer = start
            min_distance = distance
    print(f"#{test_case} {answer}")
