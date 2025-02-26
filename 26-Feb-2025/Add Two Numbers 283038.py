# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addRemaining(self,temp,l1,n):
        while l1:
            if (l1.val+n)>=10:
                temp.next = ListNode((l1.val+n)%10)
                n = (l1.val+n)//10
            else:
                temp.next = ListNode(l1.val +n)
                n = 0
            temp = temp.next
            l1 = l1.next
        return [n,temp]
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sm = ListNode()
        temp = sm
        n = 0
        while l1 and l2:
            if (l1.val + l2.val+n)>=10:
                temp.next = ListNode((l1.val + l2.val+n)%10)
                n = (l1.val + l2.val+n)//10
            else:
                temp.next = ListNode(l1.val + l2.val+n)
                n = 0
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            n,temp = self.addRemaining(temp,l1,n)
        else:
            n,temp = self.addRemaining(temp,l2,n)

        if n>0:
            temp.next = ListNode(n)

        return sm.next
                