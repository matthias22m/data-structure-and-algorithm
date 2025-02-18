# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]*(len(nums)+1)
        ans = []
        for i in range(len(nums)):
            left.append(nums[i]*left[-1])
        for i in range(len(nums)-1,-1,-1):
            right[i] = nums[i]*right[i+1]
        
        for i in range(len(nums)):
            ans.append(left[i]*right[i+1])

        return ans