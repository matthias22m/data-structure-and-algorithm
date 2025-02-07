# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    if num in rows[row] or num in cols[col]:
                        return False
                    cols[col].add(num)
                    rows[row].add(num)
        ind = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for i,j in ind:
            box = set()
            for row in range(3):
                for col in range(3):
                    num = board[row+i][col+j]
                    if num != '.':
                        if num in box:
                            return False
                        box.add(num)
            box.clear()
                    
        return True