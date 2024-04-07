# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Problem Statment
# 160. Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        tempA = headA
        while tempA:
            tempA = tempA.next
            lenA+=1

        lenB = 0
        tempB = headB
        while tempB:
            tempB = tempB.next
            lenB+=1
        
        if lenA>lenB:
            diff = lenA - lenB
            while diff:
                headA = headA.next
                diff-=1
        else:
            diff = lenB - lenA
            while diff:
                headB = headB.next
                diff-=1

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
        
