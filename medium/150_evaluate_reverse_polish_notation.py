"""
Docstring for medium.150 Code Testcase Testcase Test Result 150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operations = {"+", "-", "*", "/"}

        def cal(val1, val2, ops):
            if ops == "*":
                return val1 * val2
            elif ops == "+":
                return val1 + val2
            elif ops == "/":
                return val1 / val2
            elif ops == "-":
                return val1 - val2
            else:
                return 0

        stack = []
        for i, tkn in enumerate(tokens):
            if tkn in operations:
                val_2 = int(stack.pop(-1))
                val_1 = int(stack.pop(-1))
                stack.append(cal(val_1, val_2, tkn))
            else:
                stack.append(tkn)
        return int(stack[0])
