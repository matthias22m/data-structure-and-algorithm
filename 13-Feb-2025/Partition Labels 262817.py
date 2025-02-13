# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        _dict = {}
        mx = 0
        prev = -1
        ans = []
        for i in range(len(s)):
            _dict[s[i]] = i
        
        for i in range(len(s)):
            mx = max(mx, _dict[s[i]])
            if mx==i:
                ans.append(mx-prev)
                prev = mx
        return ans

                
        