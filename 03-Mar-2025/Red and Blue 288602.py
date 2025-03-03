# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

for _ in range(int(input())):
    n = int(input())
    r = [int(i) for i in input().split()]
    m = int(input())
    b = [int(i) for i in input().split()]

    _sum = 0
    for i in range(n):
        r[i] = r[i]+_sum
        _sum = r[i]
        if r[i] < 0:
            r[i] = 0
    
    _sum = 0
    for i in range(m):
        b[i] = b[i]+_sum
        _sum = b[i]
        if b[i] < 0:
            b[i] = 0
    
    ans = max(b)+max(r)
    print(max(ans,0))