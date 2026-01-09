# Link: https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_word = {}
        for words in strs:
            x = "".join(sorted(words))
            if x not in hash_word:
                hash_word[x] = [words]
            else:
                hash_word[x].append(words)
        return list(hash_word.values())
