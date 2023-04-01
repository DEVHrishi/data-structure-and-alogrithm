'''You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.'''

from ast import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        ans = 0
        for word in words:
            w_d = Counter(word)
            if all(d.get(ch, 0) >= w_d[ch] for ch in word):
                ans += len(word)
        return ans

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = ''
        for word in words:
            for letter in word:
                if chars.count(letter) < word.count(letter):
                    break
            else:
                ans += word
        return len(ans)