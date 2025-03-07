# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        ss = []
        for c in s:
            if c == '#':
                if ss:
                    ss.pop()
            else:
                ss.append(c)
        for c in t:
            if c == '#':
                if st:
                    st.pop()
            else:
                st.append(c)
        return st == ss