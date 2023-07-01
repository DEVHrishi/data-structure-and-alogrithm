'''A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]'''

from ast import List

# tc: o(n), sc: o(n)
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        p = []
        for i in s:
            if i == 'I':
                p.append(l)
                l += 1
            else:
                p.append(r)
                r -= 1
        if s[r-1] == 'I':
            p.append(r)
        else:
            p.append(l)
        return p
