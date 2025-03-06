# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

ln,k =  [int(i) for i in input().split()]
ls =  [int(i) for i in input().split()]

diff = []

for i in range(1,ln):
    diff.append(ls[i-1] - ls[i])
    
diff.sort()
ans = ls[-1]-ls[0]

for i in range(k-1):
    ans+=diff[i]
print(ans)