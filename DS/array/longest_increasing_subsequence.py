# Algorithm with O(nlogn)

# nums : list

def lis(nums):
    arr = []
    for x in nums:
        if not arr or x > arr[-1]:
            arr.append(x)
            continue
        for idx in range(len(arr)):
            if arr[idx] >= x:
                arr[idx] = x
                break
    return arr


# old algorithm: dynamic programming - O(N^2)
