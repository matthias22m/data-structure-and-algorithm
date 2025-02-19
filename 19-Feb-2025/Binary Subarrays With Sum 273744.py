# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        _dict = defaultdict(int)
        _dict[0]=1
        _sum = 0
        count = 0

        for num in nums:
            _sum += num
            if _sum-goal in _dict:
                count += _dict[_sum-goal]
            _dict[_sum] += 1
            
        return count