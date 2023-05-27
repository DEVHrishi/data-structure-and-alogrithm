'''You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.'''


from ast import List

# tc = O(n^m) and sc = O(1)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for word in words:
            t = 1
            for j in set(word):
                if j not in allowed:
                    t = 0
                    break
            if t == 1:
                c += 1
        return c

# tc = O(a + n * m) and sc = O(1)       
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        notSol = 0
        allowed = set(allowed)
        bitmask = 0

        for word in allowed:
            bitmask |= (1 << (ord(word) - ord('a')))

        for word in words:
            for ch in word:
                if (bitmask & (1 << (ord(ch) - ord('a')))) == 0:
                    notSol += 1
                    break

        return len(words) - notSol