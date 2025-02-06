# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = [0]+[1 if num==0 else 0 for num in nums]
        ans = []

        for i in range(1,len(nums)+1):
            zeros[i] += zeros[i-1]

        ones = [1 if num==1 else 0 for num in nums]+[0]
        for i in range(len(nums)-2,-1,-1):
            ones[i] += ones[i+1]
        
        for ind in range(len(zeros)):
            ones[ind] += zeros[ind]
        mx = max(ones)
        for i in range(len(ones)):
            if ones[i] == mx:
                ans.append(i)
        return ans

            


