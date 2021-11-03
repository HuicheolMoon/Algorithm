# Date : 2021-11-03
# 11445. 무한 사전

T = int(input())
for test_case in range(1, T + 1):
    P = input().strip()
    Q = input().strip()
    check = "Y"
    if P + 'a' == Q:
        check = "N"
    answer = f'#{test_case} {check}'
    print(answer)
