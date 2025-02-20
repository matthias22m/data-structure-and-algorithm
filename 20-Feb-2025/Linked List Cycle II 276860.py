# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while slow.next:
            if not fast or not fast.next:
                return
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        index = 0
        cur = head
        if not fast:
            return
            
        while cur != fast:
            index+=1
            cur = cur.next
            fast = fast.next
        return fast