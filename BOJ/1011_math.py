# Problem : https://www.acmicpc.net/problem/1011
# Date : 2020-02-26

import math


t = int(input())

for _ in range(t):  # for문 안의 code를 빼서 function으로 만들면 실행시간이 느려짐, 유지보수는 편하려나
    x, y = map(int, input().split())
    dis = y-x
    if dis == 1:
        print(1)
        continue
    k = math.sqrt(dis)
    if (k % 1) == 0:    # flaot 0.0 == int 0 -> True임. 재밌네
        print(2*int(k)-1)
        continue
    k = int(k)
    if dis <= (k**2 + (k+1)**2 - 1)/2:
        result = 2*k
    else:
        result = 2*k+1
    print(result)
