def select(n, x, c):
    if c == 0:
        print(x)
    s = 0 if x == [] else x[-1]+1
    for i in range(s, n):
        x.append(i)
        select(n, x, c-1)
        x.pop()

select(7, [], 4)
