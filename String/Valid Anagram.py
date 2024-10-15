'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true'''

# TC = O(n)
from collections import Counter


def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# TC = O(nlogn)
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# TC = O(n)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # naa and ana
        # an and ana

        # method 1
        # tc: O(n)+O(n)
        # calculate frequecy
        freq_of_char = Counter(s)

        for i in t:
            if i in freq_of_char:
                freq_of_char[i] -= 1
            else:
                return False
        for key, value in freq_of_char.items():
            if value != 0:
                return False
        return True

        # method 2
        # tc: O(n log n) + O(n log n) + O(n) 
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True
