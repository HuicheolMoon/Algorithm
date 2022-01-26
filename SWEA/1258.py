# [S/W 문제해결 응용] 7일차 - 행렬찾기
# Date : 2022-01-26


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    storage = [[int(i) for i in input().split()] for _ in range(n)]
    cases = []
    for y in range(n):
        for x in range(n):
            if storage[y][x] == 0:
                storage[y][x] = [0, 0]
                continue
            storage[y][x] = [1, 1]
            if y > 0:
                storage[y][x][0] = storage[y-1][x][0] + 1
            if x > 0:
                storage[y][x][1] = storage[y][x-1][1] + 1
            if (y == n-1 or storage[y+1][x] == 0) and (x == n-1 or storage[y][x+1] == 0):
                cases.append(storage[y][x])
    cases.sort(key=lambda t: (t[0]*t[1], t[0]))
    answer = " ".join([" ".join([str(i) for i in case]) for case in cases])
    print(f"#{test_case} {len(cases)} {answer}")
