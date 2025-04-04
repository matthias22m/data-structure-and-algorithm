# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[min_index],arr[i] = arr[i],arr[min_index]
        return arr