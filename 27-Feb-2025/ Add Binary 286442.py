# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sm = int(a,2)+int(b,2)
        sm = bin(sm).split('b')[1]
        return sm