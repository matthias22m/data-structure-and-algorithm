# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # Write your code here
    arr = [str(num) for num in arr]
    size = len(arr)
    key = arr[-1]
    j = size - 2
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
        print(' '.join(arr))
    arr[j + 1] = key
    print(' '.join(arr))
    return arr