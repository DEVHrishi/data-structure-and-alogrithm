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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        if a == b:
            return True
        else:
            return False
