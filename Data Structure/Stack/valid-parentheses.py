# https://leetcode.com/problems/valid-parentheses/description/
# Problem Statment
# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        
        for braces in s:
            if braces in pairs:
                stack.append(braces)
            elif len(stack) == 0 or pairs[stack.pop()] != braces:
                return False

        if len(stack)==0:
            return True
            
        
