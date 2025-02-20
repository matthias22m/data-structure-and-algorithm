# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt = head
        for i in range(n-1):
            pt=pt.next
        
        cur = ListNode(-1,head)
        while pt and pt.next:
            cur = cur.next
            pt = pt.next
        if cur.next != head:
            cur.next = cur.next.next
        else:
            head = head.next

        return head
        