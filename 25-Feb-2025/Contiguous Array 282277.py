# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _sum = 0
        prefix = [0]
        for num in nums:
            if num == 0:
                num = -1
            prefix.append(prefix[-1]+num)

        _dict = {}
        max_len = 0
        for i in range(len(prefix)):
            if prefix[i] in _dict:
                max_len = max(max_len, i-_dict[prefix[i]])
            else:
                _dict[prefix[i]] = i
        return max_len