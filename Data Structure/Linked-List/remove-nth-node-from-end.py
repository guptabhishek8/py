# https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/
# Problem Statment
# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0,head)
        temp1 = dum
        temp2 = dum

        for i in range(n+1):
            temp2 = temp2.next
        

        while temp2:
            temp1 = temp1.next
            temp2 = temp2.next

        temp1.next = temp1.next.next

        return dum.next
        

        
