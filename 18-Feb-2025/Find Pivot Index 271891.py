# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if right_sum - nums[i]-left_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1