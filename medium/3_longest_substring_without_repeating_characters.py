"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_set = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in letter_set:
                letter_set.remove(s[left])
                left += 1
            letter_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
