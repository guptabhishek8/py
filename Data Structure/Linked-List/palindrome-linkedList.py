# https://leetcode.com/problems/palindrome-linked-list/description/
# Problem Statment
# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head
        prev = None
        curr = head

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev 


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)

        while slow:
            if (head.val != slow.val):
                return False
            head = head.next
            slow = slow.next

        return True
            
        

