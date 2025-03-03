# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

ln = int(input())
ls = [int(i) for i in input().split()]

sorted_pref = [0]
pref = [0]
for i in range(ln):
    pref.append(ls[i]+pref[-1])

ls.sort()
for i in range(ln):
    sorted_pref.append(ls[i]+sorted_pref[-1])


for _ in range(int(input())):
    type,left,right = [int(i) for i in input().split()]
    if type == 1:
        print(pref[right] - pref[left-1])
    else:
        print(sorted_pref[right] - sorted_pref[left-1])
