# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Problem Statment
# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE
# Time Complexity: O(n)
# Auxiliary Space: O(h)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root!= None:
            ans.extend(self.inorderTraversal(root.left))
            ans.append(root.val)
            ans.extend(self.inorderTraversal(root.right))
        return ans

#STACK
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result (in-order traversal)
        res = []
        
        # Initialize an empty stack for iterative traversal
        stack = []
        
        # Loop until either the current node is not None or the stack is not empty
        while root or stack:
            # Traverse to the leftmost node and push each encountered node onto the stack
            while root:
                stack.append(root)
                root = root.left

            # Pop the last node from the stack (most recently left-visited node)
            root = stack.pop()
            
            # Append the value of the popped node to the result list
            res.append(root.val)
            
            # Move to the right subtree to continue the in-order traversal
            root = root.right
        
        # Return the final result list
        return res
            
        
