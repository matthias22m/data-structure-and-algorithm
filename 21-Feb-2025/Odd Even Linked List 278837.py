# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        e = even
        odd = ListNode()
        ans = odd
        cur = head
        parity = False
        

        while cur:
            if parity:
                even.next = cur
                even = even.next
            else:
                odd.next = cur
                odd = odd.next
            cur = cur.next
            parity = not parity

        odd.next = e.next
        even.next = None

        return ans.next