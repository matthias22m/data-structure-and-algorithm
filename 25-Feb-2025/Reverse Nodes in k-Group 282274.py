# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

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
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        ans = dummy

        length = 0
        while head:
            length += 1
            head = head.next

        for i in range(length//k):
            dummy = self.reverse(dummy,dummy.next,k)

        return ans.next