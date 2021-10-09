# Problem : https://programmers.co.kr/learn/courses/30/lessons/43238
# Date : 2021-10-04
# 입국심사

def solution(n, times):
    low = (n // len(times)) * min(times)
    high = (n // len(times)) * max(times)
    while low < high:
        people = 0
        mid = (low + high) // 2
        for officer in times:
            people += (mid // officer)
        if people < n:
            low = mid + 1
        else:
            high = mid
    answer = low
    return answer