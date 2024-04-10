# https://leetcode.com/problems/backspace-string-compare/
# Problem Statment
# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if len(s_stack) != 0:
                if char == "#":
                    s_stack.pop()
                    continue
            elif char == "#":
                continue
            else:
                s_stack.append(char)

        for char1 in t:
            if len(t_stack) != 0:
                if char1 == "#":
                    t_stack.pop()
                    continue
            elif char1 == "#":
                continue
            else:
                t_stack.append(char1)

        return t_stack == s_stack




        
