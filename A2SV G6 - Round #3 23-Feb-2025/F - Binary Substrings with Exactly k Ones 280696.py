# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

n = int(input())
st = input()

def atMostK(n):
    if n == -1:
        return 0
    count = 0
    left = 0
    ans = 0

    for right in range(len(st)):
        if st[right] == '1':
            count += 1
        while count > n:
            if st[left] == '1':
                count -= 1
            left += 1
        ans += right-left+1

    return ans

print(atMostK(n)-atMostK(n-1))
