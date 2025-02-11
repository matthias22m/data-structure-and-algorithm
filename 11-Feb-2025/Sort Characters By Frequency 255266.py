# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {}
        ans = []
        for char in s:
            if char not in chars:
                chars[char] = [1,char]
            else:
                chars[char][0] += 1
        vals = list(chars.values())
        vals.sort(key=lambda ls: (ls[0],-(ord(ls[1]))), reverse=True)

        for val in vals:
            for i in range(val[0]):
                ans.append(val[1])

        return ''.join(ans)
