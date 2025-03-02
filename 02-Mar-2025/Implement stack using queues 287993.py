# Problem: Implement stack using queues - https://leetcode.com/problems/implement-stack-using-queues/

from queue import Queue
class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        if not self.q1.empty():
            self.q1.put(x)
        else:
            self.q2.put(x)

    def pop(self) -> int:
        x = -1
        if not self.q1.empty():
            while not self.q1.empty():
                self.q2.put(x)   
                x = self.q1.get()
            self.q2.get()
        else:
            while not self.q2.empty():
                self.q1.put(x)   
                x = self.q2.get()
            self.q1.get()
        return x

    def top(self) -> int:
        x = -1
        if not self.q1.empty():
            while not self.q1.empty():
                x = self.q1.get()
                self.q2.put(x)   
        else:
            while not self.q2.empty():
                x = self.q2.get()
                self.q1.put(x)
        return x  
        

    def empty(self) -> bool:
        return self.q1.empty() and self.q2.empty()

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()