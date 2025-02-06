# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for k in range(i+1,len(nums)):
                    if nums[k] != 0:
                        nums[k],nums[i] = nums[i], nums[k]
                        break
        