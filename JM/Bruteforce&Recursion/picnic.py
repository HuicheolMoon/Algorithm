def picnic(students):
    if (False not in students):
        return 1
    idx = students.index(False)
    pairs = 0
    for i in range(idx+1, n):
        if (not students[i]) and (friends[idx][i] == True):
            students[idx] = True
            students[i] = True
            pairs += picnic(students)
            students[idx] = False
            students[i] = False
    return pairs


C = int(input())
for _ in range(C):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    friends =[[False for _ in range(n)] for _ in range(n)]
    for i in range(0, len(p), 2):
        friends[p[i]][p[i+1]] = friends[p[i+1]][p[i]] = True
    students = [False for _ in range(n)]
    print(picnic(students))
