# https://leetcode.com/problems/rotate-list/
# Problem Statment
# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        count = 1

        while temp and temp.next:
            temp = temp.next
            count += 1
        
        # make a circular LL
        temp.next = head

        steps =  count - (k % count)

        for i in range(steps-1):
            head = head.next

        newHead = head.next
        head.next = None

        return newHead

        
