'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false'''

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l = len(s1)
        c2 = Counter(s2[:l])
        if c1 == c2:
            return True
        for j in range(len(s2)-l):
            c2[s2[j]] -= 1
            if c2[s2[j]] == 0:
                del c2[s2[j]]
            c2[s2[j+l]] += 1
            if c1 == c2:
                return True
        return False