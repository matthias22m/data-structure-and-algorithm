# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix[0])
        row = matrix[0][:n-1]

        for ls in matrix[1:]:
            if ls[1:] != row:
                return False
            row = ls[:n-1]
        return True

