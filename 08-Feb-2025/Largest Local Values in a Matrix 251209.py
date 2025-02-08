# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ln = len(grid)
        ans = [[0]*(ln-2) for i in range(ln-2)]
        for row in range(ln-2):
            for col in range(ln-2):
                _max = 0
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        _max=max(_max,grid[i][j])
                ans[row][col] = _max
        return ans


