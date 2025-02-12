# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

a , b = map(int,input().split())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]

ans = []

top = 0
bottom = 0

while top < a and bottom < b:
    if arr1[top] < arr2[bottom]:
        ans.append(arr1[top])
        top+=1
    else:
        ans.append(arr2[bottom])
        bottom+=1
if bottom < b:
    ans.extend(arr2[bottom:])
elif top < a:
    ans.extend(arr1[top:])
print(*ans)