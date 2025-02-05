# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        ans = []
        for st in strs:
            s = ''.join(sorted(st))
            d[s].append(st)
        for k in d:
            ans.append(d[k])
        return ans
