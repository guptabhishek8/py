# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
# Problem Statment
# 1290. Convert Binary Number in a Linked List to Integer
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        # solution 1
        # ans = ""
        # while head:
        #     ans += str(head.val)
        #     head = head.next
        # return int(ans,2)
        
        # solution 2
        ans = 0
        while head:
            ans = ans*2 + head.val
            head = head.next
        return ans
