# Problem : https://leetcode.com/problems/kth-largest-element-in-an-array/
# Date : 2021-11-03


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums, reverse=True)
        answer = sorted_nums[k-1]
        return answer
