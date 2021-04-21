# Problem : https://www.acmicpc.net/problem/19663
# Date : 2020-04-21

def n_queen(loc, n):
    global count
    if len(loc) == n:
        count += 1
        return 0
    k = len(loc)
    cands = list(range(n))
    for i, q in enumerate(loc):
        if q in cands:
            cands.remove(q)
        dis = k-i
        if q+dis in cands:
            cands.remove(q+dis)
        if q-dis in cands:
            cands.remove(q-dis)
    for cand in cands:
        new_loc = loc+[cand]
        n_queen(new_loc, n)
    return 0


count = 0
n = int(input())
n_queen([], n)
print(count)


# 대부분의 백준 백트래킹 문제는 python을 사용하면 시간초과라고 한다...
