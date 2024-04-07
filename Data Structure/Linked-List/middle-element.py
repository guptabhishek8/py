# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Problem Statment
# 876. Middle of the Linked List
#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        temp1 = head
        temp2 = head

        while temp2 and temp2.next:
            temp1= temp1.next
            temp2 = temp2.next.next

        return temp1

        
