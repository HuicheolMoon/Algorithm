# Date : 2021-11-03
# 12741. 두 전구

answers = []
for test_case in range(int(input())):
    a, b, c, d = map(int, input().split())
    time = max(min(b, d) - max(a, c), 0)
    answers.append(f"#{test_case+1} {time}")
print("\n".join(answers))
