'''The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.'''

def maxPower(self, s: str) -> int:
        c,ans = 1,1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
                ans=max(c,ans)
            else:
                c=1
        return ans