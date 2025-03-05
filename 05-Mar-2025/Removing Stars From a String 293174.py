# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for char in s:
            if st and char == '*':
                st.pop()
            else:
                st.append(char)
        return ''.join(st)