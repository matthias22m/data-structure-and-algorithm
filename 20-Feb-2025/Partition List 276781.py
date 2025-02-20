# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        small = ListNode(-1)
        large = ListNode(-1)
        s = small
        l = large
        while cur:
            if cur.val >= x:
                large.next = cur
                large = large.next
                cur = cur.next
            else:
                small.next = cur
                small = small.next
                cur = cur.next
        large.next = None
        small.next = l.next
        return s.next