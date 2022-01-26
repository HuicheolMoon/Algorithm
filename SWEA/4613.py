# 러시아 국기 같은 깃발
# Date : 2022-01-26


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    min_count = n * m
    for b in range(1, n-1):
        for r in range(b+1, n):
            count = 0
            for i, line in enumerate(flag):
                if i < b:
                    count += m - line.count("W")
                elif b <= i < r:
                    count += m - line.count("B")
                elif r <= i:
                    count += m - line.count("R")
            min_count = min(min_count, count)
    print(f"#{test_case} {min_count}")
