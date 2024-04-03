# Problem Statment
# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val > list2.val:
            head = list2
            tail = list2
            list2 = list2.next
        else:
            head = list1
            tail = list1
            list1 = list1.next

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return head
           
