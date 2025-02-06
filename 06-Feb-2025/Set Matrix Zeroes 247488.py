# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zeros = set()
        col_zeros = set()
        cols = len(matrix[0])
        rows = len(matrix)
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_zeros.add(row)
                    col_zeros.add(col)

        for row in range(rows):
            for col in range(cols):
                if (row in row_zeros) or (col in col_zeros):
                    matrix[row][col] = 0
        

