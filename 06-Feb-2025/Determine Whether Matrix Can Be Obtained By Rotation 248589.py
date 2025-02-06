# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

'''
[ 00 01 02 03 04 05 ]
[ 10 11 12 13 14 15 ]
[ 20 21 22 23 24 25 ]
[ 30 31 32 33 34 35 ]
[ 40 41 42 43 44 45 ]
[ 50 51 52 53 54 55 ]

ex => 01

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
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        cols = len(mat[0])
        rows = len(mat)

        conditions = [True for i in range(4)]

        for row in range(cols):
            for col in range(cols):
                if mat[row][col] != target[row][col]:
                    conditions[0] = False
                if conditions[1]:
                    if mat[row][col] != target[col][rows-1-row]:
                        conditions[1] = False
                if conditions[2]:
                    if mat[row][col] != target[rows-1-row][rows-1-col]:
                        conditions[2] = False
                if conditions[3]:
                    if mat[row][col] != target[rows-1-col][row]:
                        conditions[3] = False
        return  sum(conditions) >= 1
                
