# link: https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for idx in range(n):
            res[idx] = prefix
            prefix *= nums[idx]
        suffix = 1
        for idx in range(n - 1, -1, -1):
            res[idx] *= suffix
            suffix *= nums[idx]
        return res
