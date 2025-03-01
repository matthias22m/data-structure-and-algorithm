# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

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
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        ans = dummy

        length = right-left+1

        while dummy.next and left>1:
            dummy = dummy.next
            left -= 1
        if dummy and dummy.next:
            self.reverse(dummy,dummy.next,length)

        return ans.next
        