# 알파벳
# Problem : https://www.acmicpc.net/problem/1987
# Date : 2022-02-24

import sys
import time


def solution(start):
    popt = 0
    addt = 0
    max_length = 1
    queue = {start}
    while queue:
        if max_length >= 26:
            return max_length, popt, addt
        tt = time.time()
        y, x, route = queue.pop()
        popt += time.time() - tt
        for m in range(4):
            ny = y + dy[m]
            nx = x + dx[m]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if arr[ny][nx] not in route:
                tt = time.time()
                queue.add((ny, nx, route+arr[ny][nx]))
                addt += time.time() - tt
                max_length = max(len(route)+1, max_length)
    return max_length, popt, addt


def solution2(start):
    popt = 0
    appendt = 0
    max_length = 1
    queue = [start]
    while queue:
        if max_length >= 26:
            return max_length, popt, appendt
        tt = time.time()
        y, x, route = queue.pop()
        popt += time.time() - tt
        for m in range(4):
            ny = y + dy[m]
            nx = x + dx[m]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if arr[ny][nx] not in route:
                tt = time.time()
                queue.append((ny, nx, route+arr[ny][nx]))
                appendt += time.time() - tt
                max_length = max(len(route)+1, max_length)
    return max_length, popt, appendt

for n in range(10, 20):
    print(f"number: {n}")
    r, c = n, n
    # arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    arr = []
    row = [chr(x+ord("A")) for x in range(n)]
    for _ in range(n):
        arr.append(row[:])
        row.append(row.pop(0))

    tt = time.time()
    print(solution((0, 0, arr[0][0])))
    print("set ", time.time() - tt)
    tt = time.time()
    print(solution2((0, 0, arr[0][0])))
    print("list ", time.time() - tt)
