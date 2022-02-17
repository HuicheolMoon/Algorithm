# 자기 방으로 돌아가기
# Date : 2022-02-17


T = int(input())
answers = []
for _ in range(T):
    n = int(input())
    times = [0 for _ in range(200)]
    for _ in range(n):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        for i in range((x-1)//2, (y-1)//2+1):
            times[i] += 1
    max_time = 0
    for i in range(200):
        if times[i] > max_time:
            max_time = times[i]
    answers.append(max_time)
for test_case in range(1, T + 1):
    print(f"#{test_case} {answers[test_case-1]}")
