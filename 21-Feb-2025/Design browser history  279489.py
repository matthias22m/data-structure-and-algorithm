# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, url='', index = 0, prev = None, next=None):
        self.url = url
        self.prev = prev
        self.next = next
        self.index = index

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def add(self,new_node, current_node):
        new_node.prev = current_node
        current_node.next = new_node

        new_node.next = self.tail
        self.tail.prev = new_node
        self.length = new_node.index

    def getHead(self):
        return self.head.next
    
    def getTail(self):
        return self.tail.prev



class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = LinkedList()
        head = self.history.head
        home_node = Node(homepage,1)
        self.history.add(home_node,head)
        self.current = home_node

        

    def visit(self, url: str) -> None:
        url_node = Node(url,self.current.index+1)
        self.history.add(url_node,self.current)
        self.current = url_node
        

    def back(self, steps: int) -> str:
        if self.current.index <= steps:
            homepage = self.history.getHead()
            self.current = homepage
            return homepage.url
        index = self.current.index - steps
        cur = self.current
        while cur:
            if cur.index == index:
                self.current = cur
                return cur.url
            cur = cur.prev

    def forward(self, steps: int) -> str:
        if self.history.length <= self.current.index + steps:
            last_page = self.history.getTail()
            self.current = last_page
            return last_page.url
        index = self.current.index + steps
        cur = self.current
        while cur:
            if cur.index == index:
                self.current = cur
                return cur.url
            cur = cur.next
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)