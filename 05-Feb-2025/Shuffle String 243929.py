# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ind_dict = {indices[i]:s[i] for i in range(len(s))}
        ls = []
        for ind in range(len(indices)):
            ls.append(ind_dict[ind])

        return ''.join(ls)