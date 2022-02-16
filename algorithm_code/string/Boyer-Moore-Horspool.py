# Boyer-Moore-Horspool algorithm
# worst case: O(nm); nm: boyer-moore algorithm itself(all correct), (+m: preprocessing)
# best case: O(n/m + m); n/m: boyer-moore algorithm itself(all incorrect), m: preprocessing
# Boyer-Moore algorithm의 simplification
# pattern 뒤에서부터 비교
# shift는 bad character table로 결정


def get_table(arr):
    # 1D table
    # for ASCII
    number = 128
    table = [len(arr) for _ in range(number)]
    for i in range(len(arr) - 1):
        table[ord(arr[i])] = len(arr) - i - 1
    return table


def boyer_moore_horspool(arr, pat):
    count = 0
    i = 0
    table = get_table(pat)
    while i <= len(arr) - len(pat):
        j = len(pat) - 1
        shift = 0
        while j >= 0:
            if pat[j] != arr[i + j]:
                shift = table[ord(pat[j])]
                break
            j -= 1
        if j == -1:
            count += 1
            i += 1
        else:
            i += shift
    return count
