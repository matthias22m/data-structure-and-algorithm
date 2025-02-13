# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = max_sum = sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            _sum -= nums[i-1]
            _sum += nums[i+k-1]
            max_sum = max(_sum,max_sum)

        return max_sum/k
