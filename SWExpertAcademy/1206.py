# Date : 2021-11-03
# 1206. [S/W 문제해결 기본] 1일차 - View

view = 2
for test_case in range(1, 11):
    L = int(input())
    B = [int(x) for x in input().split()]
    result = 0
    for i, floor in enumerate(B[view:L-view]):
        count = floor - max(B[i:i+view]+B[i+view+1:i+(2*view)+1])
        if count > 0:
            result += count
    answer = f"#{test_case} {result}"
    print(answer)
