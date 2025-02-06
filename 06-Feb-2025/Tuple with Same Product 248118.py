# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        _dict = defaultdict(int)
        ans = 0
        for n in range(len(nums)):
            for m in range(n+1,len(nums)):
                val = nums[n]*nums[m]
                _dict[val]+=1

                if (_dict[val]) > 1:
                    ans += (_dict[val]-1)


        return 8*ans

