# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        temp = None
        while head and head.next:
            cur = head.next
            head.next = temp
            cur.next,head = head,cur.next
            temp = cur
        if head:
            head.next = temp
        else:
            return temp
            
        return head

