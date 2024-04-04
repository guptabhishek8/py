# https://leetcode.com/problems/reverse-linked-list/
# Problem Statment
# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
    
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev


        
