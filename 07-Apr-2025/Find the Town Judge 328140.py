# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [0]*n
        trusted = [0]*n

        for x,y in trust:
            trusting[x-1] += 1
            trusted[y-1] += 1
        for i in range(n):
            if trusting[i] == 0 and trusted[i] == n-1:
                return i+1
        return -1
