# 가장 빠른 문자열 타이핑
# Date : 2022-02-17


T = int(input())
answers = []
for _ in range(T):
    a, b = input().split()
    count = 0
    i = 0
    while i < len(a) - len(b) + 1:
        for j in range(len(b)):
            if a[i+j] != b[j]:
                break
            if j == len(b) - 1:
                i += len(b) - 1
        i += 1
        count += 1
    count += len(a) - i
    answers.append(count)
for test_case in range(1, T + 1):
    print(f"#{test_case} {answers[test_case-1]}")
