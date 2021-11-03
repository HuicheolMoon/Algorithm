# Problem : https://leetcode.com/problems/product-of-array-except-self/
# Date : 2021-11-03


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_mutiple = 1
        answer = [0 for _ in range(len(nums))]
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_mutiple *= num
            if zero_count >= 2:
                return answer
        if zero_count == 1:
            answer[nums.index(0)] = total_mutiple
            return answer
        for i, num in enumerate(nums):
            answer[i] = total_mutiple // num
        return answer
