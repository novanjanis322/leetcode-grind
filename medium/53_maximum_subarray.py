# Link: https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
