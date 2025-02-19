# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        _dict = defaultdict(int)
        _dict[0]=1
        _sum = 0
        count = 0

        for num in nums:
            _sum += num
            if _sum-k in _dict:
                count += _dict[_sum-k]
            _dict[_sum] += 1
            
        return count