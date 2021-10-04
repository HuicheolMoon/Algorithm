# AC
# Problem : https://www.acmicpc.net/problem/5430
# Date : 2020-02-25

from sys import stdin
from collections import deque

t = int(stdin.readline())
for _ in range(t):
    p = stdin.readline()
    n = int(stdin.readline())
    nums = deque()
    arr = stdin.readline().rstrip()[1:-1].split(",")
    if n != 0:
        nums.extend(arr)
    error = False
    mode = True
    for cmd in p:
        if cmd == "R":
            mode = not mode
        elif cmd == "D":
            if len(nums) == 0:
                error = True
                break
            elif mode:
                nums.popleft()
            else:
                nums.pop()
    if error:
        print("error")
    else:
        if not mode:
            nums.reverse()
        print("[" + ",".join(nums) + "]")
