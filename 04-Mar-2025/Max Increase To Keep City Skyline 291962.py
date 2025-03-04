# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col = [0]*len(grid)
        row = [0]*len(grid)

        for i in range(len(grid)):
            r_max = 0
            c_max = 0
            for j in range(len(grid)):
                r_max = max(r_max,grid[i][j])
                c_max = max(c_max,grid[j][i]) 
            row[i] = max(r_max,row[i])
            col[i] = max(c_max,col[i])
        diff = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                diff += min(col[i],row[j]) - grid[i][j]
        return diff

