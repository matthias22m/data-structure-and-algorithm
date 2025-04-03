# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        pointer = new_head

        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                pointer = pointer.next
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next
        if list1:
            pointer.next = list1
        if list2:
            pointer.next = list2

        return new_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = None
        fast = head
        slow = head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.mergeTwoLists(left,right)