# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        rows=len(matrix)
        cols=len(matrix[0])

        visited = set()
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        turn = 0
        row,col = 0,0
        
        for i in range(rows*cols):
            ans.append(matrix[row][col])
            visited.add((row,col))
            n_row,n_col = row+direction[turn][0],col+direction[turn][1]

            if not (0 <= n_row<rows and 0<=n_col<cols) or ((n_row,n_col) in visited):
                turn = (turn+1)%4
                row,col = row+direction[turn][0],col+direction[turn][1]
            elif (n_row,n_col) not in visited:
                    row = n_row
                    col = n_col

        return ans
