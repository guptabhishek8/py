# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Problem Statment
# 1669. Merge In Between Linked Lists
# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1 = list1
        
        for i in range(a-1):
            temp1 = temp1.next

        temp2 = temp1.next
        for i in range(a,b+1):
            temp2 = temp2.next

        temp1.next = list2
        while temp1.next:
            temp1 = temp1.next

        temp1.next = temp2

        return list1

        
        
