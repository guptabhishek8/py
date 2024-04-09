# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Problem Statment
# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the 
# list's nodes (i.e., only nodes themselves may be changed.)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev = ListNode()
        curr = head
        head = head.next


        while curr and curr.next:
            temp = curr.next.next

            prev.next = curr.next 
            curr.next.next = curr
            curr.next = temp
            prev = curr
            curr = curr.next

        return head





        
