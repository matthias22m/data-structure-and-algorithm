# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    mx = arr[0]
    for score in arr:
        if mx >score:
            print(score)
            break
    else:
        print(mx)