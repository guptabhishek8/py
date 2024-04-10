# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Problem Statment
# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        temp = head
        val = temp.val
        while temp and temp.next:
            if val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
                val = temp.val
        return head
        
