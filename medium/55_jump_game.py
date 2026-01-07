# link: https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        n = len(nums)
        for i in range(n):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
            if reachable >= n - 1:
                return True
        return True
