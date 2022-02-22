# 로봇 청소기
# Problem : https://www.acmicpc.net/problem/14503
# Date : 2022-02-22

def is_in_arr(ny, nx):
    return 0 <= ny < n and 0 <= nx < m


n, m = map(int, input().split())
y, x, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0
while True:
    if arr[y][x] == 0:
        arr[y][x] = 2
        answer += 1
    count = 0
    while count < 4:
        d = (d - 1) % 4
        ny = y + dy[d]
        nx = x + dx[d]
        if is_in_arr(ny, nx) and arr[ny][nx] == 0:
            y, x = ny, nx
            break
        count += 1
    if count == 4:
        d = (d - 2) % 4
        ny = y + dy[d]
        nx = x + dx[d]
        if not is_in_arr(ny, nx) or arr[ny][nx] == 1:
            break
        else:
            y, x = ny, nx
            d = (d - 2) % 4
print(answer)
