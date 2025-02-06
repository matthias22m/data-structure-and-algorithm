# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transpose = [[0]*rows for i in range(cols)]
        for row in range(rows):
            for col in range(cols):
                transpose[col][row] = matrix[row][col]
        return transpose