"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        x = nums.copy()
        nums.sort()
        dict_nums = {}
        dict_nums[nums[0]] = 0
        n = len(nums)
        sum = 1
        for i in range(1, n):
            if nums[i] not in dict_nums:
                dict_nums[nums[i]] = sum
            sum += 1
        for num in x:
            res.append(dict_nums[num])
        return res
