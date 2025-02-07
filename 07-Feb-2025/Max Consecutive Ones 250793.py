# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [str(i) for i in nums]
        nums = ''.join(nums)
        nums = nums.split('0')
        _max = 0
        for num in nums:
            _max = max(len(num),_max)
        return _max