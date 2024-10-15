'''You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.'''

# TC = O(n)
def reformat(self, s: str) -> str:
        a = [c for c in s if c.isalpha()]
        b = [c for c in s if c.isdigit()]
        if len(a) < len(b): a, b = b, a
        if len(a) - len(b) > 1: return ""
        
        rv = []
        while a:
            rv.append(a.pop())
            if b: rv.append(b.pop())
        return rv
        