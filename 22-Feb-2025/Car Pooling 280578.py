# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ls = [0]*1001
        for num,fr, to in trips:
            ls[fr]+=num
            ls[to]-=num
        for i in range(1,1001):
            ls[i] += ls[i-1]
            if ls[i-1] > capacity:
                return False
        return True
        