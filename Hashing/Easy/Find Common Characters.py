'''Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]'''

from ast import List
import string


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabet = string.ascii_lowercase
        d = {c: 0 for c in alphabet}
        
        for k, v in d.items():
            d[k] = min([word.count(k) for word in A])

        res = []
        for c, n in d.items():
            if n > 0:
                res += [c] * n
        return res