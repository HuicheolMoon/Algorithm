# [S/W 문제해결 응용] 10일차 - 작업순서
# Date : 2022-01-26


for test_case in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))
    array = []
    parents = [[] for _ in range(v+1)]
    while edges:
        end = edges.pop()
        start = edges.pop()
        parents[end].append(start)
    vertices = list(range(1, v+1))
    while vertices:
        for vertex in vertices:
            if not parents[vertex]:
                vertices.remove(vertex)
                array.append(vertex)
                for other in vertices:
                    if vertex in parents[other]:
                        parents[other].remove(vertex)
    answer = " ".join([str(i) for i in array])
    print(f"#{test_case} {answer}")
