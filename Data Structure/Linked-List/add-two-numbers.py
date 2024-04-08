# https://leetcode.com/problems/add-two-numbers/description/
# Problem Statment
# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        carry = 0
        while l1 or l2 or carry:
            data1 = 0
            data2 = 0
            if l1:
                data1 = l1.val
                l1 = l1.next
            if l2:
                data2 = l2.val
                l2 = l2.next
            
            finalSum = data1+data2 + carry
            carry = finalSum//10

            temp.next = ListNode((finalSum)%10)
            temp = temp.next


        return head.next


        
        
