# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                for k in range(i+1,len(nums)):
                    if nums[k] != 0:
                        nums[k],nums[i] = nums[i], nums[k]
                        break
        return nums

            
                    