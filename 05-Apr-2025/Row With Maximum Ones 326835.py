# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        _max = [0,0]
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count+=1
            if _max[1] < count:
                _max = [i,count]
        return _max