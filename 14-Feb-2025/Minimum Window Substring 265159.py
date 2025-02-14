# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def compare(self, window: Counter, count: Counter) -> bool:
        for char in count:
            if char not in window:
                return False
            if count[char] > window[char]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s),len(t)
        current = Counter()
        count = Counter(t)
        left = 0        
        ans = [inf,0,0]
        

        for right in range(m):

            current[s[right]] += 1
            while right-left+1 >= n and self.compare(current,count):
                if ans[0] > right-left+1:
                    ans[0] = right-left+1
                    ans[1] = left
                    ans[2] = right
                current[s[left]] -= 1
                left += 1  
        if ans[0] == inf:
            return ""

        return s[ans[1]:ans[2]+1]