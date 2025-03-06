# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if st:
                    st.pop()
            else:
                st.append(log)
        return len(st)