# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        for i in range(ln):
            j = i+1
            while j < ln:
                if nums[i] < 0 :
                    break
                if nums[j] < 0:
                    j+=1
                    continue

                if nums[i] == nums[j]:
                    nums[i] = -1
                    nums[j] = -1
                j+=1
        leftovers = [i for i in nums if i >= 0]
        return [(ln-len(leftovers))//2,len(leftovers)]
            
