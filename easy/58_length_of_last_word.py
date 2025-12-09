"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Link: https://leetcode.com/problems/length-of-last-word

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split(" ")[-1]
        print(last_word)
        return len(last_word)
