# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if sum(nums) == 0 and k == 0:
            return 0
        _max = 0
        left = 0
        right = 0
        zeros = 0
        cur = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                while zeros > k and left < right:
                    if nums[left] == 0:
                        zeros -= 1
                    left+=1
            right+=1
            
            _max = max(right-left,_max)
        return _max