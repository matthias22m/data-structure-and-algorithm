# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        ans = []
        d = defaultdict(list)

        for i in range(rows):
            for j in range(cols):
                d[i+j].append(mat[i][j])

        for k in range(rows+cols):
            if k%2 == 0:
                d[k].reverse()
            ans += d[k]
        return ans

            