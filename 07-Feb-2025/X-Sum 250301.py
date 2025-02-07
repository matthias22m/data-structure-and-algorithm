# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def solve():
    for _ in range(int(input())):
        mat = []
        rows,cols = map(int,input().split())

        for i in range(rows):
            row = [int(i) for i in input().split()]
            mat.append(row)
        ans = 0
            
        for r in range(rows):
            for c in range(cols):
                i,j = r,c
                _sum = 0
                while i>=0 and j>=0:
                    _sum += mat[i][j]
                    i,j= i-1,j-1
                
                i,j = r,c

                while i<rows and j<cols:
                    _sum += mat[i][j]
                    i,j= i+1,j+1
                i,j = r,c
                
                while i>=0 and j<cols:
                    _sum += mat[i][j]
                    i,j= i-1,j+1
                i,j = r,c

                while i<rows and j>=0:
                    _sum += mat[i][j]
                    i,j= i+1,j-1

                _sum -= mat[r][c]*3

                ans = max(_sum,ans)
        print(ans)
                

solve()