# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        cnt['1'] -= 1

        ans = ['1']*cnt['1']
        for i in range(cnt['0']):
            ans.append('0')
            
        ans.append('1')

        return ''.join(ans)