# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = [int(i) for i in input().split()]
pref  = [0]*200002
mx = 0
for i in range(n):
    start,end = [int(i) for i in input().split()]
    
    pref[start]+=1
    pref[end+1]-=1

for i in range(1,200001):
    pref[i+1] += pref[i]

    if pref[i] >= k:
        pref[i] = 1
    else: 
        pref[i] = 0

for i in range(1,200002):
    pref[i] += pref[i-1]

for i in range(q):
    left,right = map(int,input().split())

    print(pref[right]-pref[left-1])