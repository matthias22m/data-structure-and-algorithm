# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

from queue import Queue
class RecentCounter:


    def __init__(self):
        self.ls = []
        self.head = 0
        self.len = 0

    def ping(self, t: int) -> int:
        while self.len > self.head and self.ls[self.head] < t-3000:
            self.head += 1
            
        self.ls.append(t)
        self.len += 1
        
        return self.len-self.head

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)