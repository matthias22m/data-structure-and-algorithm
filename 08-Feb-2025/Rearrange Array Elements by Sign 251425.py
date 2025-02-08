# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos = []
        neg = []
        for num in nums:
            pos.append(num) if num>0 else neg.append(num)

        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans