# 가장 긴 바이토닉 부분 수열
# Problem : https://www.acmicpc.net/problem/11054
# Date : 2020-02-25

n = int(input())
arr_l = list(map(int, input().split()))

dp_l = [1 for _ in range(n)]
for i in range(1, n):
    cands_l = arr_l[:i]
    dp_l[i] = max([dp_l[j] for j, x in enumerate(cands_l) if x < arr_l[i]] + [0]) + 1

arr_r = arr_l[::-1]

dp_r = [1 for _ in range(n)]
for i in range(1, n):
    cands_r = arr_r[:i]
    dp_r[i] = max([dp_r[j] for j, x in enumerate(cands_r) if x < arr_r[i]] + [0]) + 1

dp = [x + y - 1 for x, y in zip(dp_l, dp_r[::-1])]
print(max(dp))
