# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        range_sum = [0]*(len(nums)+1)
        for i,j in requests:
            range_sum[i]+=1
            range_sum[j+1]-=1

        for i in range(1,len(range_sum)):
            range_sum[i] += range_sum[i-1]

        range_sum.sort(reverse=True)
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]*range_sum[i]
        return _sum % (10**9 + 7)