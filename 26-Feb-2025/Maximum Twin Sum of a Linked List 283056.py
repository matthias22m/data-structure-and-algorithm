# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node,cur,k):
        for i in range(k-1):
            temp = cur.next
            cur.next = temp.next
            temp.next = node.next
            node.next = temp
        return cur

    def pairSum(self, head: Optional[ListNode]) -> int:
        ln = 0
        start = head
        while head:
            ln+=1
            head = head.next
        temp = start
        ind = 0
        while ind < ln//2-1:
            temp = temp.next
            ind+=1
        
        self.reverse(temp,temp.next,ln//2)
        mx = 0
        mid = temp.next
        while mid:
            mx = max(mx,mid.val+start.val)
            start=start.next
            mid=mid.next

        return mx