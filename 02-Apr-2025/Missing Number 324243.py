# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for num in range(0,len(nums)+1):
            if num not in nums:
                return num
