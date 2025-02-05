# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        _sum = 0
        ans = []
        for num in nums:
            if num%2==0:
                _sum += num

        for val, ind in queries:
            nums[ind]+=val
            if nums[ind]%2 == 0 and val%2 != 0:
                _sum+=nums[ind]
            elif nums[ind]%2 != 0 and val%2 != 0:
                _sum-= (nums[ind]-val)
            elif nums[ind]%2 == 0 and val%2 == 0:
                _sum+=val
            ans.append(_sum)
            
        return ans


            
