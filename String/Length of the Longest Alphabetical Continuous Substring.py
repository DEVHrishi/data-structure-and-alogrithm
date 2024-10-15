'''An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

Example 1:

Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
Example 2:

Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.'''

# tc : O(n) and sc : O(1)
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i = 0
        j = 1
        mx = 0
        while j < len(s):
            if ord(s[j]) == ord(s[j-1]) + 1:
                j += 1
            else:
                mx = max(mx, len(s[i:j]))
                i = j
                j += 1
        return max(mx, len(s[i:j]))

