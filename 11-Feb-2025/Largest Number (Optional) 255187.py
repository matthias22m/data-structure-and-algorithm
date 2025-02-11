# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=lambda num: num*10, reverse=True)   
        if nums[0] == '0':
            return '0'     
        return ''.join(nums)