# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

'''
row0 1
col0 0

row1 = col0 -> 0
col1 = rows - 1 - row0 -> 4

row2 = rows - 1  - row0 -> 4
col2 = rows -1 - col0 -> 5

row3 = rows - 1 - col0 -> 5
col3 = row0 -> 0
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        ln = len(matrix)
        for row in range(ln):
            for col in range(ln):
                if (row,col) in visited:
                    continue
                ls = [[row,col],[col,ln-1-row],[ln-1-row,ln-1-col],[ln-1-col,row]]
                for i,j in ls:
                    visited.add((i,j))

                matrix[row][col],matrix[ln -1 - col][row] = matrix[ln -1 - col][row],matrix[row][col]
                matrix[ln -1 - col][row],matrix[ln - 1  - row][ln -1 - col] = matrix[ln - 1  - row][ln -1 - col],matrix[ln -1 - col][row]
                matrix[ln - 1  - row][ln -1 - col],matrix[col][ln-1-row] = matrix[col][ln-1-row],matrix[ln - 1  - row][ln -1 - col]
