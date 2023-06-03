'''You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"'''

# tc = O(n) and sc = O(n)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for i in s:
            if l and i == l[-1]:
                l.pop()
            else:
                l.append(i)
        return ''.join(l)

# tc = O(n) and sc = O(1)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        idx =0
        while(idx+1<len(s)):
            if(s[idx]==s[idx+1]):
                s= s[:idx]+s[idx+2:]
                if idx > 0:
                    idx -= 1
            else:
                idx += 1
        return s