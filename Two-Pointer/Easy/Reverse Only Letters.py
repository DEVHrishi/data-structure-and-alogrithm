'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"'''

import string

# tc = O(n) and sc = O(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabets=list(string.ascii_letters)
        l = 0
        r = len(s) - 1
        x = list(s)
        while (l < r):
            if x[l] not in alphabets:
                l += 1
            elif x[r] not in alphabets:
                r -= 1
            else:
                x[l], x[r] = x[r], x[l]
                l += 1
                r -= 1
        return (''.join(x))