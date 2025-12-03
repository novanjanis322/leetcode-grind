"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Link: https://leetcode.com/problems/find-pivot-index

"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum_left = [0] * n
        sum_right = [0] * n
        for i in range(1, n):
            sum_left[i] = nums[i - 1] + sum_left[i - 1]
        for j in range(n - 2, -1, -1):
            sum_right[j] = nums[j + 1] + sum_right[j + 1]
        print(sum_left, sum_right)
        for i in range(n):
            if sum_left[i] == sum_right[i]:
                return i
        return -1