# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        _sum = 0
        mn = 0
        for i in range(len(nums)):
            if _sum + nums[i] > 0:
                _sum = 0
                continue
            _sum += nums[i]
            mn = min(mn,_sum)
        _sum = 0
        mx = 0
        for i in range(len(nums)):
            if nums[i]+_sum < 0:
                _sum = 0
                continue
            _sum += nums[i]
            mx = max(mx,_sum)
        return max(mx,abs(mn))