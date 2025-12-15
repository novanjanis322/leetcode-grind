"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

Link: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] == "(":
                    stack.pop(-1)
                    continue
                else:
                    return False
            if char == "]":
                if len(stack) == 0:
                    return False
                if stack[-1] == "[":
                    stack.pop(-1)
                    continue
                else:
                    return False
            if char == "}":
                if len(stack) == 0:
                    return False
                if stack[-1] == "{":
                    stack.pop(-1)
                    continue
                else:
                    return False
            stack.append(char)
        if len(stack) > 0:
            return False
        return True
