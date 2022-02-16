# Knuth–Morris–Pratt algorithm
# O(N+M); N: kmp algorithm itself, M: lps preprocessing
# 실패함수 lps(longest proper prefix which is also suffix)를 이용하여 pattern 앞에서부터 비교


def get_lps(arr):
    lps = [0] * len(arr)
    length = 0
    i = 1
    while i < len(arr):
        if arr[i] == arr[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length-1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp(arr, pat):
    lps = get_lps(pat)
    i = 0
    j = 0
    count = 0
    while i < len(arr):
        if pat[j] == arr[i]:
            i += 1
            j += 1
        elif pat[j] != arr[i] and j != 0:
            j = lps[j-1]
        elif pat[j] != arr[i]:
            i += 1
        if j == len(pat):
            count += 1
            j = lps[j-1]
    return count
