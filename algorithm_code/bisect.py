# Python bisect lib; https://github.com/python/cpython/blob/main/Lib/bisect.py

# arr = sorted array

def bisect_left(arr, x):
    # x 이상 원소 중 최솟값의 index
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low


def bisect_right(arr, x):
    # x 초과 원소 중 최솟값의 index (= x 이하 원소 중 최댓값의 index + 1)
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low
