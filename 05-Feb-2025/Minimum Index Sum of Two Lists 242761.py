# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        _min = inf
        _dict = {}
        ans = []
        for i,val in enumerate(list1):
            _dict[val] = i
        
        for ind, st in enumerate(list2):
            if st in _dict:
                if _min > _dict[st] + ind:
                    _min = _dict[st] +ind
                    ans.clear()
                    ans.append(st)
                elif _min == _dict[st]+ind:
                    ans.append(st)

        return ans