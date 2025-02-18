# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if right_sum - nums[i]-left_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1