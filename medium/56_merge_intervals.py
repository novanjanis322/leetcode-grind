# Link: https://leetcode.com/problems/merge-intervals/description/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        ans = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans
