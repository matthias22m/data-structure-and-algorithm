# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i] > st[-1][0]:
                val,ind = st.pop()
                ans[ind] = i-ind
            st.append((temperatures[i],i)) 
        return ans
